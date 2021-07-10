from django.urls import path
from . import views

app_name = 'imoveis'

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('cadastrar_imovel/', views.cadastrar_imovel, name='cadastrar_imovel'),
    path('gerenciar_imoveis/', views.gerenciar_imoveis, name='gerenciar_imoveis'),
    path('agendar_estadia/<int:imovel_id>', views.agendar_estadia, name='agendar_estadia'),
    path('editar_imovel/<int:imovel_id>', views.editar_imovel, name='editar_imovel'),
    path('deletar_imovel/<int:imovel_id>', views.deletar_imovel, name='deletar_imovel'),
]