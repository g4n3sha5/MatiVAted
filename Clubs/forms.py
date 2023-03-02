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
        'class': 'form-control w-100 text-center',
        'placeholder': 'Academy name',
        'autocomplete' : 'do-not-autofill',

    }), required=False)

    logo = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'imageInput'
    }), required=False)

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' form-control p-2 mx-0 h-100 text-center  ',
        'spellcheck': 'false',
        'placeholder': 'Write a short description...'
    }), required=False)

    estabilished = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center',
        'placeholder': 'Year of foundation (optional)'
    }), required=False)


    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100 h-100 text-center ',
        'placeholder': 'Address...'
    }), required=False)

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100  text-center',
        'placeholder': 'Postal code (optional), City'
    }), required=False)

    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center',
        'placeholder': 'Phone number(s) 615 515 242, 555 555 555 '
    }), required=False)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center ',
        'placeholder': 'Contact email (optional)'
    }), required=False)

    website = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center ',
        'placeholder': 'Website (optional) [www.example.com or example.com]'
    }), required=False)

class MemberForm(ModelForm):
    class Meta:
        model = UserMembership
        fields = ['authorized', 'memberType']

    authorized = forms.ChoiceField(choices = UserMembership.AUTHORIZED,
                                   required=False)
    memberType = forms.ChoiceField(choices = UserMembership.MEMBER_TYPES,
                                   required=False)
    # favGrappler = forms.CharField(widget=form.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Favourite grappler'
    # }), required=False)

class ScheduleForm(forms.Form):
    # NIE DZIALA????????????
    time = forms.CharField(
        widget=forms.TimeInput(

        attrs={
            'class': 'timepicker',
            'type': 'time',

    }),  required=True)

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 h-100 text-center',
        'placeholder': 'Short description...',
        'maxlength' : 60
    }), required=False)
