from django.shortcuts import render, redirect
from date.forms import DateVehicleForm

from date.models import DateVehicle


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
