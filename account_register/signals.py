from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def create_profile(sender, **kwargs):
    myuser = kwargs['user']
    UserProfile.objects.create(user = myuser)

