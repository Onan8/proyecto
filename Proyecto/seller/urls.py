from django.urls import path
from . import views

urlpatterns = [
    path('', views.seller_list, name='seller_list'),
    path('new/', views.seller_create, name='seller_create'),
    path('<int:pk>/', views.seller_detail, name='seller_detail'),
    path('<int:pk>/edit/', views.seller_update, name='seller_update'),
    path('<int:pk>/delete/', views.seller_delete, name='seller_delete'),
]
