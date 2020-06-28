from django.contrib import admin
from engine.models.TimeSlot import TimeSlot, TimeSlotForVendor
from engine.models.Event import Event
# Register your models here.

admin.site.register(TimeSlot)
admin.site.register(TimeSlotForVendor)
admin.site.register(Event)
