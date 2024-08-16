from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from user.models import User
from client.models import Client
from seller.models import Seller

def index(request):
    return render(request, 'account/index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Intentar autenticar en el modelo `User`
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect('index')  # Redirigir  usuario o a otra página

            # Intentar autenticar en el modelo `Client`
            try:
                client = Client.objects.get(email=cd['username'])
                if client.check_password(cd['password']):
                    request.session['client_id'] = client.id  # Guardar información en la sesión
                    return redirect('index')
            except Client.DoesNotExist:
                pass

            # Intentar autenticar en el modelo `Seller`
            try:
                seller = Seller.objects.get(email=cd['username'])
                if seller.check_password(cd['password']):
                    request.session['seller_id'] = seller.id  # Guardar información en la sesión
                    return redirect('index')
            except Seller.DoesNotExist:
                pass

            return HttpResponse('Credenciales inválidas o cuenta deshabilitada.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
