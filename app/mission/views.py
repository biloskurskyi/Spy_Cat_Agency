from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Goal, Mission

from .serializers import MissionSerializer


class MissionCreateView(APIView):
    """
    Create Mission
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MissionDeleteView(APIView):
    """
    Delete Mission
    """
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
            if not mission.can_be_deleted():
                return Response({'detail': 'Mission cannot be deleted because it is assigned to a cat.'},
                                status=status.HTTP_400_BAD_REQUEST)
            mission.delete()
            return Response({'detail': 'Mission deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Mission.DoesNotExist:
            return Response({'detail': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)
