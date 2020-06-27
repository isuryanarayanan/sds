from django.db import models
# Create your models here.


class Event(models.Model):

    customer = models.ForeignKey(
        "accounts.customer_profile", on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        "accounts.vendor_profile", on_delete=models.CASCADE)
    datetime = models.ForeignKey("engine.TimeSlot", on_delete=models.CASCADE)

    class Meta:
        app_label = "engine"
