from django.db import models
# Create your models here.


class TimeSlot(models.Model):
    """
    Time slot is the standard for events in the app
    """
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        app_label = "engine"

    def save(self, *args, **kwargs):
        if self.end > self.start:
            raise ValueError("Time interval is not valid")
        super(TimeSlot, self).save(*args, **kwargs)


class TimeSlotForVendor(models.Model):

    start = models.TimeField()
    end = models.TimeField()
    interval = models.IntegerField()

    class Meta:
        app_label = "engine"

    def save(self, *args, **kwargs):
        if self.end < self.start:
            raise ValueError("Time interval is not valid")
        self.interval = self.end.minute - self.start.minute
        if self.interval < 5:
            raise ValueError("Time interval should be greater than 5")
        super(TimeSlotForVendor, self).save(*args, **kwargs)
