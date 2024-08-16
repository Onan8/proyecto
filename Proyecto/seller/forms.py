from django import forms
from .models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'age', 'number_employee', 'phone', 'address', 'number_id', 'email', 'schedule', 'location', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        seller = super().save(commit=False)
        raw_password = self.cleaned_data['password']
        seller.set_password(raw_password)
        if commit:
            seller.save()
        return seller