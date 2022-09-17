from webbrowser import MacOSX
from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(label='Name', max_length=255, required=True)
    email = forms.EmailField(label='Email', max_length=255, required=True)
    content = forms.CharField(label='Content', max_length=500, widget=forms.Textarea)