from django.contrib import admin
from django.urls import path
from agendamentos.views import  agendamento, criar_servicos, editar_servicos, listar_servicos, servicos,excluir

urlpatterns = [
    path("",servicos, name="servicos"),
    path('agendamento/',agendamento,name="agendamento"),
    path("listar_servicos/",listar_servicos,name='listar_servicos'),
    path("criar_servicos/",criar_servicos,name='criar_servicos'),
    path("editar_servicos/<int:servico_id>",editar_servicos,name='editar_servicos'),
    path("excluir/<int:servico_id>",excluir,name='excluir')
    
]