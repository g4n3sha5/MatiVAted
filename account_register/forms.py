from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from .models import UserProfile
from .models import *


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user']

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' form-control p-2 mx-0 h-100 text-center',
        'spellcheck': 'false',
        'placeholder': 'Write a short bio...'
    }), required=False)

    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'First name',
    }), required=False)

    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Last name'
    }), required=False)

    belt = forms.ChoiceField(choices=UserProfile.belts,
                             widget=forms.RadioSelect(),
                             required=False)

    favGrappler = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Favourite grappler'
    }), required=False)

    favTechnique = forms.ModelChoiceField(queryset=Technique.objects.all(),
                                widget=forms.RadioSelect(),
                                required=False,
                                # initial=
                                          )

    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'imageInput'
    }), required=False)