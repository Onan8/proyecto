from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['email', 'name', 'age', 'number_employee', 'phone', 'address', 'number_id']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Crear una instancia de usuario sin guardar aún
        user = super().save(commit=False)
        # Establecer la contraseña usando el método `set_password`
        user.set_password(self.cleaned_data["password1"])
        # Guardar la instancia si `commit` es True
        if commit:
            user.save()
        return user
