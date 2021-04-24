from django.urls import path
from . import views

app_name = 'institucional'

urlpatterns = [
    path('', views.home, name='home'),
    path('quem_somos', views.quem_somos, name='quem_somos'),
]