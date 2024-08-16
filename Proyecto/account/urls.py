from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    #urls para loguearse y cerrar seccion
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #pagina de inicio
    path('', index, name='index'),

]