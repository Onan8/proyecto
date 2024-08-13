from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserCreateForm
from django.contrib.auth import logout
from django.urls import reverse


# Create your views here.
#cerrar secion
def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))

#lista todos los usuarios administradores
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

#muestra un solo usuario
@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user/user_detail.html', {'user': user})

#crea un nuevo usuario
@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreateForm()
    return render(request, 'user/user_form.html', {'form': form})

#actualiza un solo usuario
@login_required
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

#para eliminar un usuario
@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user/user_confirm_delete.html', {'user': user})