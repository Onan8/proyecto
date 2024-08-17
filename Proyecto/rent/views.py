from django.shortcuts import render, redirect

from rent.forms import RentalVehicleForm
from rent.models import RentalVehicle
from user import views as user_views


# Create your views here.
def list_rent(request):
    vehicles = RentalVehicle.objects.all()
    return render(request, 'rent/index_rent.html', {'vehicles': vehicles})


def create_vehicle_rent(request):
    if request.method == 'POST':
        form = RentalVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index_rent')
    else:
        form = RentalVehicleForm()
        return render(request, 'rent/rent_form.html', {'form': form})


def detail_vehicle_rent(request, pk):
    vehicle = RentalVehicle.objects.get(pk=pk)
    return render(request, 'rent/detail_vehicle_rent.html', {'vehicle': vehicle})


def delete_vehicle_rent(request, pk):
    vehicle = RentalVehicle.objects.get(pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('index_rent')
    return render(request, 'rent/confirm_delete_rentVehicle.html', {'vehicle': vehicle})
