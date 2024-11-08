import re

from decouple import config
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    """
    Custom User model for the application.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.name} with email {self.email}"

    def set_password(self, raw_password):
        """
        Set the password for the user after validating its strength.
        """
        if len(raw_password) < int(config('PASSWORD_LENGTH')):
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', raw_password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        super().set_password(raw_password)
