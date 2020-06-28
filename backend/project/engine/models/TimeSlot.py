from django.db import models
# Create your models here.


class TimeSlot(models.Model):

    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        app_label = "engine"

    def save(self, *args, **kwargs):
        if self.end > self.start:
            raise ValueError("Time interval is not valid")
        super(TimeSlot, self).save(*args, **kwargs)
