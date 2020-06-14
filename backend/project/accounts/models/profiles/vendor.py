from django.db import models
from accounts.models.user import User
# Create your models here.


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
        app_label = "accounts"

    def __str__(self):
        return f'{self.first_name} | {self.user.email}'
