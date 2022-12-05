from django.db import models
from django import forms
from django.forms import ModelForm
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
    addedByUser = models.ManyToManyField(User, related_name="user_session", blank=False)


    def __str__(self):
        return self.type, self.date


# form for addSession, addSession.html
class DatePickerInput(forms.DateInput):

    input_type = 'datetime'


class TrainingSessionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': field.label})
            # print(field.widget.attrs)
    class Meta:
        model = TrainingSession
        exclude = ('type', 'addedByUser')
