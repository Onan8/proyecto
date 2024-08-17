from django.shortcuts import render, redirect

from rent.forms import RentalVehicleForm
from rent.models import RentalVehicle, Rental
from client.models import Client
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


def delete_rental(request, pk):
    rental = Rental.objects.get(pk=pk)
    if request.method == 'POST':
        rental.delete()
        return redirect('index_rent')
    return render(request, 'rent/confirm_delete_rentVehicle.html', {'rental': rental})


def save_rent(request):
    if request.method == "POST":
        vehicle = request.POST['vehicle']
        vehicle_instance = RentalVehicle.objects.get(pk=vehicle)
        client = request.POST['client']
        dayEntrance = request.POST['dayEntrance']
        dayExit = request.POST['dayExit']
        client_instance = Client.objects.get(pk=client)
        rental = Rental(RentalVehicle=vehicle_instance, client=client_instance, dayEntrance=dayEntrance, dayExit=dayExit)
        rental.save()
    return redirect('index_rent')
