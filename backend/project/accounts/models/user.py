from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
# Create your models here.

"""
User modes decide which permissions each user will recieve
"""
user_modes = (
    (1, 'customer'),
    (2, 'vendor'),
    (3, 'administrator')
)


class User(AbstractUser):

    email = models.EmailField(unique=True)
    mode = models.IntegerField(choices=user_modes, default=1)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        app_label = "accounts"
