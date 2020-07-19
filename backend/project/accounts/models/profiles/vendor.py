from django.db import models
from accounts.models.user import User
from engine.models.TimeSlot import TimeSlot, TimeSlotForVendor
from engine.engine import checkTestsForSlots
from django.core.exceptions import ValidationError
import datetime
# Create your models here.


class vendor_profile(models.Model):
    """
    Profile for vendor users
    """
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Calendar
    """
    Calendar requirements
    - should not be overlapping
    - start time and end time should be valid
    - date should be forward
    """
    calendar = models.ManyToManyField(TimeSlot, blank=True)

    # Time slot for customers
    """
    Time slot requirements
    - start and end should be valid
    - interval should be converted to minutes
    """
    # timeslot = models.ForeignKey(
    #     TimeSlotForVendor, on_delete=models.CASCADE, null=True)
    timeslot = models.IntegerField(default=1)

    class Meta:
        verbose_name = "vendor profile"
        verbose_name_plural = "vendor profiles"
        app_label = "accounts"

    def __str__(self):
        return f'{self.user.email}'

    # def save(self, *args, **kwargs):
    #     calendar = []

    #     for cal in self.calendar.all():
    #         calendar.append(cal)

    #     resp = checkTestsForSlots(calendar)
    #     if resp == True:
    #         super(vendor_profile, self).save(*args, **kwargs)
    #     else:
    #         raise ValidationError("Error in slot")
