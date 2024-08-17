from django.shortcuts import render, redirect
from client.models import Client
from date.forms import DateVehicleForm
from date.models import DateVehicle, Date
from rent.models import RentalVehicle


# Create your views here.
def list_date(request):
    vehicles = DateVehicle.objects.all()
    return render(request, 'date/index_date.html', {'vehicles': vehicles})


def create_vehicle_date(request):
    if request.method == 'POST':
        form = DateVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index_date')
    else:
        form = DateVehicleForm()
        return render(request, 'date/date_form.html', {'form': form})


def detail_vehicle_date(request, pk):
    vehicle = DateVehicle.objects.get(pk=pk)
    return render(request, 'date/detail_vehicle_date.html', {'vehicle': vehicle})


def delete_vehicle_date(request, pk):
    vehicle = DateVehicle.objects.get(pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('index_date')
    return render(request, 'date/confirm_delete_dateVehicle.html', {'vehicle': vehicle})


def save_date(request):
    if request.method == "POST":
        vehicle = request.POST['vehicle']
        vehicle_instance = DateVehicle.objects.get(pk=vehicle)
        client = request.POST['client']
        client_instance = Client.objects.get(pk=client)
        dateDay = request.POST['dayDate']
        date = Date(DateVehicle=vehicle_instance, client=client_instance, daydate=dateDay)
        date.save()
    return redirect('index_date')


def delete_date(request, pk):
    date = Date.objects.get(pk=pk)
    if request.method == 'POST':
        date.delete()
        return redirect('index_date')
    return render(request, 'date/confirm_delete_date.html', {'date': date})
