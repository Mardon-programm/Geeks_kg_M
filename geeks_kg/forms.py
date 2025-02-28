from django import forms
from .models import ContactForm  # Импортируем модель

class ContactFormForm(forms.ModelForm):  # Название формы
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'age', 'phone_number']  # Поля формы
