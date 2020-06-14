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
    start = models.TimeField(auto_now=True)
    # End time depicts the end of the slot
    end = models.TimeField(auto_now=True)

    class Meta:
        app_label = "event"

    def clean(self):
        """
        Checking time slot to be truthful,
        the time slot should not exceed what the limit of the vendor should be        
        """
        start = [self.start.hour, self.start.minute, self.start.second]
        end = [self.end.hour, self.end.minute, self.end.second]
        # # Checking time slot to be truthful
        # if start[0] > end[0] :
        #     raise ValidationError("Invalid hours.")
        # else if start[0] <= end[0]:

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
