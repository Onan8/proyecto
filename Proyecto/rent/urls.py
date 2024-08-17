from django.urls import path
from . import views

urlpatterns = [
    path('index/rent/', views.list_rent, name='index_rent'),
    path('vehicle/new/', views.create_vehicle_rent, name='create_vehicle_rent'),
    path('detailVehicle/<int:pk> ', views.detail_vehicle_rent, name='detail_vehicle_rent'),
    path('vehicle/delete/<int:pk> ', views.delete_vehicle_rent, name='delete_vehicle_rent'),
    path('save/rent', views.save_rent, name='save_rent'),
    path('rental/delete/<int:pk> ', views.delete_rental, name='delete_rental'),
]
