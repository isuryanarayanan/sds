from django.db import models
from datetime import datetime
# Create your models here.


class Event(models.Model):

    customer = models.ForeignKey(
        "accounts.customer_profile", on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        "accounts.vendor_profile", on_delete=models.CASCADE)
    datetime = models.ForeignKey("engine.TimeSlot", on_delete=models.CASCADE)

    class Meta:
        app_label = "engine"

    def ValidateSlots(self):
        # The Event timeslot
        end_minutes = self.datetime.end.hour*60 + self.datetime.end.minute
        start_minutes = self.datetime.start.hour*60 + self.datetime.start.minute
        difference = end_minutes - start_minutes  # The interval in the event
        print(difference)
        print(self.vendor.timeslot.interval)
        if self.vendor.timeslot.interval >= difference:
            pass
        else:
            raise ValueError("Time slot is not valid for the vendor")
        # Check here that the slot fits in the interval

    def save(self, *args, **kwargs):
        self.ValidateSlots()  # The validate function checks if the datetime fits in the slot
        super(Event, self).save(*args, **kwargs)
