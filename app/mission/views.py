from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Cat, Goal, Mission

from .serializers import GoalSerializer, MissionSerializer


class MissionCreateView(APIView):
    """
    Create Mission
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
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
        except Mission.DoesNotExist:
            return Response({'detail': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

        if mission.owner != request.user:
            return Response({'detail': 'You do not have permission to delete this mission.'},
                            status=status.HTTP_403_FORBIDDEN)

        if not mission.can_be_deleted():
            return Response({'detail': 'Mission cannot be deleted because it is assigned to a cat.'},
                            status=status.HTTP_400_BAD_REQUEST)

        mission.delete()
        return Response({'detail': 'Mission deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class MissionUpdateView(APIView):
    """
    Update Mission (assign cat to mission).
    """
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            return Response({'detail': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

        if mission.owner != request.user:
            return Response({'detail': 'You do not have permission to modify this mission.'},
                            status=status.HTTP_403_FORBIDDEN)

        if mission.is_completed:
            return Response({'detail': 'Mission is completed. No updates allowed.'},
                            status=status.HTTP_400_BAD_REQUEST)

        cat_id = request.data.get('cat_id')
        if cat_id:
            try:
                cat = Cat.objects.get(id=cat_id)

                if cat.owner != request.user:
                    return Response({'detail': 'You can only assign cats that belong to you.'},
                                    status=status.HTTP_403_FORBIDDEN)

                mission.cat = cat
                mission.save()
            except Cat.DoesNotExist:
                return Response({'detail': 'Cat not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'detail': 'Mission updated successfully, cat assigned.'}, status=status.HTTP_200_OK)


class GoalUpdateView(APIView):
    """
    Update Goal details (status, notes).
    """
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            goal = Goal.objects.get(pk=pk)
        except Goal.DoesNotExist:
            return Response({'detail': 'Goal not found.'}, status=status.HTTP_404_NOT_FOUND)

        mission = goal.mission

        if mission.owner != request.user:
            return Response({'detail': 'You do not have permission to update goals of this mission.'},
                            status=status.HTTP_403_FORBIDDEN)

        if mission.is_completed:
            return Response({'detail': 'Mission is completed. No updates allowed.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if goal.status:
            return Response({'detail': 'Cannot edit notes for a completed goal.'},
                            status=status.HTTP_400_BAD_REQUEST)

        goal.status = request.data.get('status', goal.status)
        goal.notes = request.data.get('notes', goal.notes)

        goal.save()

        return Response({'detail': 'Goal updated successfully.', 'goal': GoalSerializer(goal).data},
                        status=status.HTTP_200_OK)


class MissionsGet(APIView):
    """
    List of all missions.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        missions = Mission.objects.filter(owner=request.user)
        serializer = MissionSerializer(missions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MissionGetById(APIView):
    """
    Get mission by ID.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk, owner=request.user)
        except Mission.DoesNotExist:
            return Response({"message": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MissionSerializer(mission)
        return Response(serializer.data, status=status.HTTP_200_OK)
