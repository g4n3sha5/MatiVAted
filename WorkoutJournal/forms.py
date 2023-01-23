from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from .models import *


class DatePickerInput(forms.DateInput):
    input_type = 'datetime'



class TrainingSessionForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields['addedByUser'].initial = user

    class Meta:
        model = TrainingSession
        fields = '__all__'

    type = forms.ChoiceField(choices=TrainingSession.TStypes, widget=forms.RadioSelect())

    notes = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' BJRnotes form-control mx-3 h-100',
        'spellcheck': 'false',
        'placeholder': 'Training notes...'
    }), required=False)

    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'datepicker-input',
        'type': 'date'
    }), required=False)

    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location...'

    }), required=False)

    length = forms.ChoiceField(choices=TrainingSession.TSlength,
                               widget=forms.RadioSelect())

    techniques = forms.ModelMultipleChoiceField(queryset=Technique.objects.all(),
                                                widget=forms.CheckboxSelectMultiple(),
                                                required=False)
        # widget=forms.CheckboxSelectMultiple(attrs={'class':'techniqueOption list-group-item p-2 d-flex '
        #                                                  'align-items-center cursor-pointer justify-content-between '
        #                                                  'mb-1 d-block bg-transparent'}))
    # widget=TechniquesCheckBox())


class addTechniqueForm(ModelForm):
    type = forms.ChoiceField(choices=Technique.TechniqueTypes, widget=forms.RadioSelect())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         # Field('type', css_class='sessionType', template="BJR_Techniques_types.html"),
    #         Field('type', css_class='sessionType'),
    #         Field('EnglishName', css_class='form-control'),
    #         Field('otherName', css_class='form-control'),
    #         # Field('description', css_class='form-control mb-3')
    #     )

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
