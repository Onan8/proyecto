from django.shortcuts import render, get_object_or_404, redirect
from client.models import Client
from date.models import DateVehicle
from seller.models import Seller
from .models import User
from .forms import UserCreateForm
from rent.models import RentalVehicle, Rental
from date.models import DateVehicle, Date


#modelo CRUD
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user/user_detail.html', {'user': user})


def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreateForm()
    return render(request, 'user/user_form.html', {'form': form})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreateForm(instance=user)
    return render(request, 'user/user_form.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user/user_confirm_delete.html', {'user': user})


#funcion para redirigir al admin a su pagina de inicio
def user_index(request, pk):
    users = User.objects.all()
    clients = Client.objects.all()
    sellers = Seller.objects.all()
    vehicle_rents = RentalVehicle.objects.all()
    vehicle_dates = DateVehicle.objects.all()
    rental = Rental.objects.all()
    dates = Date.objects.all()

    #a;ade lo demas aqui e importa sus models no olvides importarlos

    return render(request, 'user/user_index.html', {
        'users': users,
        'clients': clients,
        'sellers': sellers,
        'vehicle_rents': vehicle_rents,
        'vehicle_dates': vehicle_dates,
        'rental': rental,
        'dates': dates
        #a;adelos de esta manera
    })
