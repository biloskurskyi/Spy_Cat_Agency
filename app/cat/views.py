from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Cat

from .serializers import CatSerializer


class CatView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Create new cat.
        """
        serializer = CatSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        List of all cats.
        """
        cats = Cat.objects.filter(owner=request.user)
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CatDetailView(APIView):
    """
    View to retrieve, update, or delete a specific cat.
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            cat = Cat.objects.get(pk=pk, owner=request.user)
        except Cat.DoesNotExist:
            return Response({"message": "Cat not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CatSerializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            cat = Cat.objects.get(pk=pk, owner=request.user)
        except Cat.DoesNotExist:
            return Response({'detail': 'Cat not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CatSerializer(cat, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
