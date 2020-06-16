from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class OpenInCalendar(models.Model):
    """ 
    Calendar holds all the openings the vendor have 
    through out their operation inorder to indicate
    to customers that when the vendor is available 
    to book an appointment. 
    """
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        app_label = "calendar_app"

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must be after starting times')

    def save(self, *args, **kwargs):
        super(OpenInCalendar, self).save(*args, **kwargs)
