from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/new/', views.user_create, name='user_create'),
    path('user/<int:pk>/edit/', views.user_update, name='user_update'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),

# URLs para inicio de sesión y cierre de sesión
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
