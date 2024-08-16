from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', index, name='index'),

]