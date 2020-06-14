from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models.user import User
from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
from accounts.models.profiles.administrator import administrator_profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.mode == 1:
            customer = customer_profile.objects.create(user=instance)
        if instance.mode == 2:
            vendor = vendor_profile.objects.create(user=instance)
        if instance.mode == 3:
            administrator = administrator_profile.objects.create(user=instance)
