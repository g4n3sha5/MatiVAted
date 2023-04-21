from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100 text-center mb-2',
        'placeholder': 'Title'
    }), required=False)

    content = notes = forms.CharField(widget=forms.Textarea(attrs={
        'class': ' form-control  h-100',
        'spellcheck': 'false',
        'placeholder': 'Content...'
    }), required=False)