from django import forms
from .models import Cours, ContactForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm  
        fields = ['first_name', 'last_name', 'age', 'phone_number'] 