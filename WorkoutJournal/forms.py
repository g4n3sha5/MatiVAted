from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms
from django.forms import ModelForm
from .models import *



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
            Field('type', css_class='sessionType'),
            Field('EnglishName', css_class='form-control'),
            Field('otherName', css_class='form-control'),
            Field('description', css_class='form-control mb-3')
        )


    class Meta:
        model = Technique
        fields = '__all__'

# class descriptionSuggestion(forms.Form):
#     # content = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 120}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'class' : ' rounded-2 p-2'}))

class descriptionSuggestion(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': ' rounded-2 p-2',
            'spellcheck' : 'false'
        }))

    class Meta:
        model = Suggestion
        fields = ('content',)