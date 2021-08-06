from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from  django.db.models.signals import post_save
from django.contrib.auth import  get_user_model
from accounts.models import Profile

User = get_user_model()

from .models import Profile

# @receiver(user_signed_up) 
# def populate_profile(user, **kwargs):

#     user.profile = Profile()   

#     user.profile.user = user
#     user.profile.save()

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

      
