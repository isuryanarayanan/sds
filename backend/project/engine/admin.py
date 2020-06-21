from django.contrib import admin
from engine.models.TimeSlot import TimeSlot
from engine.models.Event import Event
# Register your models here.

admin.site.register(TimeSlot)
admin.site.register(Event)
