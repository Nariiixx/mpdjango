from django.urls import path
from . import views

urlpatterns = [
    path('', views.phome, name='phome'),
    path('cadastro/', views.pcadastro, name='pcadastro'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('localizar/', views.localizar, name='localizar'),
    path('lista_produtos/', views.lista_de_produto, name='lista_de_produto'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
    path('deletar/', views.deletar_produto, name='deletar_produto'),
    path('api/dashboard/', views.dashboard_dados, name='dashboard_dados')

]