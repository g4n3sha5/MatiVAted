from django.db import models
from django import forms
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class Technique (models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class TrainingSession(models.Model):
    TStypes = (
        ('GI', 'Gi'),
        ('NOGI', 'No Gi'),
        ('GYM', 'Gym')
    )

    type = models.CharField(choices=TStypes, blank=False, max_length=16)
    date = models.DateField(default=date.today)
    location = models.CharField(max_length=50)
    length = models.IntegerField()
    notes = models.CharField(max_length=300)
    techniques = models.ForeignKey(Technique, on_delete=models.CASCADE, null = True)
    user_session = models.ManyToManyField(User, related_name="user_session", blank=False)


    def __str__(self):
        return self.type, self.date



# form for addSession, addSession.html

class DatePickerInput(forms.DateInput):
    input_type = 'datetime'


class addSessionForm(forms.Form):
    # type = forms.ChoiceField(choices=TrainingSession.TStypes, blank=False, max_length=16)
    length = forms.IntegerField()
    date = forms.DateTimeField(widget=DatePickerInput)
    location = forms.CharField(label="Location (optional)", max_length=50, required=False)
    notes = forms.CharField(max_length=300)

    # techniques = models.ForeignKey(Technique, on_delete=models.CASCADE, null=True)