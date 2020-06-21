from django.db import models
from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
# Create your models here.


class Event(models.Model):

    customer = models.ForeignKey(customer_profile, on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendor_profile, on_delete=models.CASCADE)

    class Meta:
        app_label = "engine"
