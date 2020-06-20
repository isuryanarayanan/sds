from django.db import models
from accounts.models.user import User
from engine.models import TimeSlot
from engine.engine import checkTestsForSlots
from django.core.exceptions import ValidationError
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
        calendar = []

        for cal in self.calendar.all():
            calendar.append(cal)

        resp = checkTestsForSlots(calendar)
        if resp == True:
            super(vendor_profile, self).save(*args, **kwargs)
        else:
            raise ValidationError("Error in slot")
