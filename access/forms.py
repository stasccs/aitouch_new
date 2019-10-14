from django import forms


class RegForm(forms.Form):

    login = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'id': 'login'}))
    pass1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    pass2 = forms.CharField(widget=forms.PasswordInput(), label='Подтверждение пароля')
    email = forms.EmailField(label='Электронная почта')


class EntryForm(forms.Form):

    login = forms.CharField(label='Логин', error_messages={'required': 'pole jest'})
    pass1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

