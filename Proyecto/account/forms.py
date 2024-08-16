
from django import forms
from django.shortcuts import redirect, render


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Email ',
            'class': 'login__input'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'login__input'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username



