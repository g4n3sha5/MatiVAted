from django.db import models
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from WorkoutJournal.models import Technique

# Create your models here.

class UserProfile(models.Model):
    belts = (
        ('No Info', 'No Info'),
        ('White Belt', 'White Belt'),
        ('Blue Belt', 'Blue Belt'),
        ('Purple Belt', 'Purple Belt'),
        ('Brown Belt', 'Brown Belt'),
        ('Black Belt', 'Black Belt')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20, blank=True, null=True, default = 'User')
    lastName = models.CharField(max_length=20, blank=True, null=True, default = 'Anonymous')
    avatar = models.ImageField(default='default.png', upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(max_length=256, blank=True, null=True)
    belt = models.CharField(choices=belts, max_length=16, default=belts[0][0])
    favTechnique = models.ForeignKey(Technique, on_delete=models.CASCADE, blank=True, null=True)
    favGrappler = models.CharField(max_length=40, blank=True, null=True)
    # academy
