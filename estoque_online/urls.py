from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.phome, name='phome'),
    path('home/cadastro/', views.pcadastro, name='pcadastro'),
    path('home/atualizar/', views.atualizar, name='atualizar'),
    path('home/localizar/', views.localizar, name='localizar'),
    path('home/lista_produtos/', views.lista_de_produto, name='lista_de_produto'),
    path('home/relatorio/', views.relatorio, name='relatorio')
]