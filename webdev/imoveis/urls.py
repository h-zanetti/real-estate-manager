from django.urls import path
from . import views

app_name = 'imoveis'

urlpatterns = [
    path('catalogo', views.catalogo, name='catalogo'),
    # path('agendar_estadia/<int:imovel_id>', views.agendar_estadia, name='agendar_estadia'),
]