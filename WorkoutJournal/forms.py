# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from Clubs.views import userClub
from .models import *


class DatePickerInput(forms.DateInput):
    input_type = 'datetime'



class ClubTrainingSession(forms.Form):
    # club = forms.BooleanField(widget= forms.CheckboxInput(), initial = False,required=False)
   club = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={"class": "form-check-input", "id": "flexSwitchCheckDefault"}),
    required=False)


class TrainingSessionForm(ModelForm):
    # def __init__(self, userID, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.fields['club']:
    #         self.fields['club'] = userClub(userID)
    #     else:
    #         self.fields['club'] = None
    class Meta:
        model = TrainingSession
        fields = '__all__'

    type = forms.ChoiceField(choices=TrainingSession.TStypes, widget=forms.RadioSelect())

    notes = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' BJRnotes form-control  h-100',
        'spellcheck': 'false',
        'placeholder': 'Training notes...'
    }), required=False)

    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'datepicker-input w-100',
        'type': 'date'
    }), required=False)

    timestamp = forms.TimeField(widget=forms.TimeInput(attrs={
        'class':'timepicker',
        'type' :'time'
    }), required=False)


    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location...'

    }), required=False)

    hoursLength = forms.ChoiceField(choices=TrainingSession.HOURS_LENGTH,
                                    widget=forms.RadioSelect())

    minutesLength = forms.ChoiceField(choices=TrainingSession.MINUTES_LENGTH,
                                      widget=forms.RadioSelect(),
                                      required=False)

    fightTime = forms.IntegerField(required = False,
                                   widget=forms.NumberInput(
                                       attrs={
                                           'class': 'fightTimeInput form-control',
                                            'min': 0,
                                            'max': 400,
                                            'value' : 0,
                                           'type': 'number'
                                           # 'placeholder': 'min'
                                       }))


    techniques = forms.ModelMultipleChoiceField(queryset=Technique.objects.all(),
                                                widget=forms.CheckboxSelectMultiple(),
                                                required=False)



    # widget=forms.CheckboxSelectMultiple(attrs={'class':'techniqueOption list-group-item p-2 d-flex '
    #                                                  'align-items-center cursor-pointer justify-content-between '
    #                                                  'mb-1 d-block bg-transparent'}))
    # widget=TechniquesCheckBox())


class addTechniqueForm(ModelForm):
    type = forms.ChoiceField(choices=Technique.TechniqueTypes, widget=forms.RadioSelect())


    class Meta:
        model = Technique
        fields = '__all__'


class descriptionSuggestion(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': ' rounded-2 p-2',
            'spellcheck': 'false'
        }))

    class Meta:
        model = Suggestion
        fields = ('content',)
