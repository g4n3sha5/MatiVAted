
from django.db import models
from django import forms
from django.forms import ModelForm
from datetime import date
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from crispy_forms.bootstrap import InlineRadios
# Create your models here.


class Technique (models.Model):
    TechniqueTypes = (
        ('Choke', 'Choke'),
        ('Throw', 'Throw'),
        ('Lever', 'Lever'),
        ('Sweep', 'Sweep'),
        ('Position', 'Position')
    )
    type = models.CharField(choices=TechniqueTypes, max_length=15)
    EnglishName = models.CharField(max_length=42, blank=False, unique=True)
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
    class Meta:
        model = TrainingSession
        exclude = ('type', 'addedByUser')



class addTechniqueForm(ModelForm):
    type = forms.ChoiceField(choices=Technique.TechniqueTypes, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            # Field('type', css_class='sessionType', template="BJR_Techniques_types.html"),
            Field('type', css_class='sessionType', template="BJR_Techniques_types.html"),
            Field('EnglishName', rows="3", css_class='form-control'),
            Field('otherName', css_class='form-control'),
            Field('description', css_class='form-control mb-3')
        )


    class Meta:
        model = Technique
        fields = '__all__'
