from django.db import models
from django import forms
from django.forms import ModelForm
from datetime import date
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
# Create your models here.


class Technique (models.Model):
    TechniqueTypes = (
        ('Choke', ' Choke'),
        ('Throw', 'Throw'),
        ('Lever', 'Lever'),
        ('Sweep', 'Sweep'),
        ('Position', 'Position')
    )
    type = models.CharField(choices=TechniqueTypes, max_length=15)
    EnglishName = models.CharField(max_length=42)
    otherName = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.EnglishName


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
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class': field.label})
    #         # print(field.widget.attrs)
    # class Meta:
    #     model = TrainingSession
    #     exclude = ('type', 'addedByUser')

class addTechniqueForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('type', css_class='row addSession techniqueType justify-content-between px-5'),
            Field('EnglishName', rows="3", css_class='form-control mb-3'),
            Field('otherName', css_class='form-control mb-3'),
            Field('description', css_class='form-control mb-3'),
        )


    class Meta:
        model = Technique
        fields = '__all__'

        # widgets = {
        #     'type': forms.ChoiceField(,
        #     attrs={'class': 'form-control'}),
        #     # 'EnglishName': TextInput(attrs={'class': 'form-control'}),
        #     # 'otherName': Textarea(attrs={'class': 'form-control'}),
        #     # 'description': Select(attrs={'class': 'form-control'})
        # }