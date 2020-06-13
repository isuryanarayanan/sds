from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User
from accounts.models import customer_profile, vendor_profile, administrator_profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.mode == 1:
            customer = customer_profile.objects.create(user=instance)
        if instance.mode == 2:
            vendor = vendor_profile.objects.create(user=instance)
        if instance.mode == 3:
            administrator = administrator_profile.objects.create(user=instance)
