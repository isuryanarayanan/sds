from django.db import models
from accounts.models.user import User
# Create your models here.


class customer_profile(models.Model):
    """
    Profile for customer users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Verbal identifiers
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')

    class Meta:
        verbose_name = "customer profile"
        verbose_name_plural = "customer profiles"
        app_label = "accounts"

    def __str__(self):
        return f'{self.first_name} | {self.user.email}'
