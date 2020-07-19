from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from accounts.models.user import User
from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
from accounts.models.profiles.administrator import administrator_profile
from engine.engine import checkTestsForSlots


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.mode == 1:
            customer = customer_profile.objects.create(user=instance)
        if instance.mode == 2:
            vendor = vendor_profile.objects.create(user=instance)
        if instance.mode == 3:
            administrator = administrator_profile.objects.create(user=instance)


@receiver(post_save, sender=vendor_profile)
def validate_calendar(sender, instance=None, created=False, **kwargs):
    calendar = []
    for cal in instance.calendar.all():
        calendar.append(cal)
    resp = checkTestsForSlots(calendar)

    if resp == True:
        print("Slot Validated")
    else:
        print("Error in slot")
