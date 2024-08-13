from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'identity', 'email', 'age', 'telephone', 'license', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
