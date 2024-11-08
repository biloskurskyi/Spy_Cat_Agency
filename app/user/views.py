import datetime

import jwt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User

from .serializers import UserSerializer


class RegisterView(APIView):
    """
    Handles user registration. Validates the provided data, creates a new user.

    POST request data should include 'email' and 'password'.
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    Authenticates a user and provides a JWT token upon successful login.

    POST request data should include 'email' and 'password'.
    """

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password) or not user.is_active:
            raise AuthenticationFailed('User not found or password is incorrect')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({'jwt': token, 'id': user.id})


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)  # Перевірка, чи авторизований користувач

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logged out successfully'
        }
        return response


class DeleteUserView(APIView):
    """
    Allows an user to delete their own account.

    Requires authentication.
    """
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        user = request.user
        if user.id != request.user.id:
            return Response({'error': 'You can only delete your own account.'}, status=status.HTTP_400_BAD_REQUEST)

        user.delete()

        return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
