from django.db import models
from accounts.models.user import User
from calendar_app.models import OpenInCalendar
from django.core.exceptions import ValidationError
# Create your models here.


class vendor_profile(models.Model):
    """
    Profile for vendor users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=250, default='')

    # Calendar
    calendar = models.ManyToManyField(OpenInCalendar)

    # Time slot
    time_gap_in_mins = models.IntegerField(default=15)

    class Meta:
        verbose_name = "vendor profile"
        verbose_name_plural = "vendor profiles"
        app_label = "accounts"

    def clean(self):
        if self.time_gap_in_mins == 0:
            raise ValidationError("Time gap should be greater than 0")

    def __str__(self):
        return f'{self.vendor_name} | {self.user.email}'
