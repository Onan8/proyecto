from django import forms
from .models import DateVehicle


class DateVehicleForm(forms.ModelForm):
    class Meta:
        model = DateVehicle
        fields = ['tradeMark', 'vehicleModel', 'year', 'numberDoors', 'parking', 'transmission', 'vehicleType', 'price',
                  'image']
