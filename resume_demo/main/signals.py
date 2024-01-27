# creating user profile using signals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

# Signal is a way that we can indicate something to happen at an instant or anytime
# Types of signals : pre_save, post_save, pre_delete, post_delete
# The receiver decorator is a way to connect a function to a signal.
# It works like : create an entry whenever this / that things happen.

# whenever the User object is created , it will hit this signal
# to make it workable , we'll use ready method in apps.py

# In conclusion , here when the user profile is created in admin dashboard the user automatically gets the signal and get into creation in UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)