from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your models here.

class NewUser (UserCreationForm):
    email = forms.EmailField(required = True )
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']