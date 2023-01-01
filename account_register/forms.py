from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from .models import UserProfile
from .models import *


class UserProfileForm(ModelForm):
    belt = forms.ChoiceField(choices=UserProfile.belts, widget=forms.RadioSelect())
    class Meta:
        model = UserProfile
        fields = '__all__'
