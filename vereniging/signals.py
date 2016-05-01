# File signals created on: 30-04-16 by: ejah
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from . import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.Gebruiker(user=instance)
    profile.save()