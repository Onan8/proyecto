from django.urls import path
from . import views

urlpatterns = [
    path('index/date/', views.list_date, name='index_date'),
    path('date/new', views.create_vehicle_date, name='create_vehicle_date'),
    path('date/detailVehicle/<int:pk>', views.detail_vehicle_date, name='detail_vehicle_date'),
    path('vehicle/delete/<int:pk>', views.delete_vehicle_date, name='delete_vehicle_date'),

]