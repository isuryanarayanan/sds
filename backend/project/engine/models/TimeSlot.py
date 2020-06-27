from django.db import models
# Create your models here.


class TimeSlot(models.Model):

    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        app_label = "engine"
