from django.urls import path

from .views import (DeleteUserView,
                    LoginView, LogoutView, RegisterView)

app_name = 'user'

"""
URL patterns for user-related operations including registration, login, logout, and user deletion.
"""

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/', DeleteUserView.as_view(), name='delete_library_user'),
]
