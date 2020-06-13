from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
# from .managers import UserManager
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


class customer_profile(models.Model):
    """
    Profile for customer users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Verbal identifiers
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "customer profile"
        verbose_name_plural = "customer profiles"


class vendor_profile(models.Model):
    """
    Profile for vendor users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Verbal identifiers
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "vendor profile"
        verbose_name_plural = "vendor profiles"


class administrator_profile(models.Model):
    """
    Profile for administrator users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Verbal identifiers
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "administrator profile"
        verbose_name_plural = "administrator profiles"
