from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control',
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control',
        })