from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    SUPERUSER = 1
    STAFF = 2
    EMPLOYEE = 3
    CUSTOMER = 4

    USER_TYPE = (
        (SUPERUSER, 'superuser'),
        (STAFF, 'staff'),
        (EMPLOYEE, 'employee'),
        (CUSTOMER, 'customer')
    )


    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
