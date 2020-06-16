from django.db import models
from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
from django.core.exceptions import ValidationError


class Event(models.Model):
    """ Event is when a customer books a time slot with the vendor """
    # Customer will create the event.
    customer = models.ForeignKey(customer_profile, on_delete=models.CASCADE)
    # Vendor will accept/reject the event
    vendor = models.ForeignKey(vendor_profile, on_delete=models.CASCADE)
    # Day of event
    day = models.DateField()
    # Time slot for the event
    # Start time depicts the begining of the slot
    start_time = models.TimeField(auto_now=True)
    # End time depicts the end of the slot
    end_time = models.TimeField(auto_now=True)

    class Meta:
        app_label = "event"

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:
            overlap = True

        return overlap

    def clean(self):
        """
        Checking time slot to be truthful,
        the time slot should not exceed what the limit of the vendor preset.      
        """
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day, vendor=self.vendor)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
