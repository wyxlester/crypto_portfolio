import shortuuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

# This file is used to generate a referral code for each user as soon as they sign up.
def generate_referral_code():
    return shortuuid.ShortUUID().random(length=10)

# This signal code generates a referral code for a user as soon as they sign up. It does this by listening for the "post_save" signal from the User model.
# When a new User instance is created, this signal triggers the "create_profile" function which creates a Profile instance for that user and generates a unique referral code using shortuuid library.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, referral_code=generate_referral_code())
        # This generated referral code is then saved to the Profile instance.
        profile.save()
