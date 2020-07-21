from django.db import models
from accounts.models.user import User
# Create your models here.


class CalendarEventManager(models.Manager):
    def create_calendar_event(self, day, start, end, valid=False):
        cal = self.model(
            day=day,
            start=start,
            end=end,
            valid=valid
        )
        cal.save()


class CalendarEvent(models.Model):
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    valid = models.BooleanField(default=False)

    class Meta:
        app_label = "engine"

    def save(self, *args, **kwargs):
        if self.end < self.start:
            raise ValueError("Time interval is not valid")
        super(CalendarEvent, self).save(*args, **kwargs)


class CalendarManager(models.Manager):
    def create_calendar(self, user, events=None, active=False):
        cal = self.model(
            user=user,
            events=events,
            active=active
        )
        cal.save()


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(CalendarEvent)
    active = models.BooleanField(default=False)
    objects = CalendarManager()
