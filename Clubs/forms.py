from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from .models import Club
from .models import *


class ClubForm(ModelForm):
    class Meta:
        model = Club
        exclude = ['authorizedUser', 'instructors']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-75 text-center',
        'placeholder': 'Academy name',
        'autocomplete' : 'do-not-autofill',

    }), required=False)

    logo = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'imageInput'
    }), required=False)

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' form-control p-2 mx-0 h-100',
        'spellcheck': 'false',
        'placeholder': 'Write a short description...'
    }), required=False)

    estabilished = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-50',
        'placeholder': 'Year of foundation (optional)'
    }), required=False)


    location = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100 ',
        'placeholder': 'Location of academy...'
    }), required=False)

    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center',
        'placeholder': 'Contact phone number(s)'
    }), required=False)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center ',
        'placeholder': 'Contact email (optional)'
    }), required=False)

    website = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center ',
        'placeholder': 'Website (optional)'
    }), required=False)




    # favGrappler = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Favourite grappler'
    # }), required=False)

