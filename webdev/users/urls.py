from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('ser_anfitriao/', views.ser_anfitriao, name='ser_anfitriao'),
]