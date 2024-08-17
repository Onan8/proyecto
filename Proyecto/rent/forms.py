from django import forms
from .models import RentalVehicle


class RentalVehicleForm(forms.ModelForm):
    class Meta:
        model = RentalVehicle
        fields = ['tradeMark', 'vehicleModel', 'year', 'numberDoors', 'parking', 'transmission', 'vehicleType', 'price',
                  'image']
