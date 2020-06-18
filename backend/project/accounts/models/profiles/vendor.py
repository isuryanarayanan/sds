from django.db import models
from accounts.models.user import User
from engine.models import TimeSlot
# Create your models here.


class vendor_profile(models.Model):
    """
    Profile for vendor users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Calendar
    calendar = models.ManyToManyField(TimeSlot)

    class Meta:
        verbose_name = "vendor profile"
        verbose_name_plural = "vendor profiles"
        app_label = "accounts"

    def __str__(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        super(vendor_profile, self).save(*args, **kwargs)
