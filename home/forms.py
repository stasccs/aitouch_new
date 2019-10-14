from django import forms


# Модель формы обратной связи

my_default_errors = {
    'required': 'To pole jest wymagane',
    'invalid': 'Wprowadź poprawne dane'
}


class ContactForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'To pole jest wymagane'}, max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'To pole jest wymagane', 'placeholder': 'Imię', 'style': 'margin-bottom: 20px'}))
    email = forms.EmailField(error_messages=my_default_errors, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'style': 'margin-bottom: 20px'}))
    message = forms.CharField(error_messages=my_default_errors, label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Wiadomość', 'style': 'margin-bottom: 20px'}))
