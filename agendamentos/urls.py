from django.contrib import admin
from django.urls import path
from agendamentos.views import  agendamento, agendar, criar_horario, criar_servicos,  editar_horario, editar_servicos, excluir_horario, horarios, listar_servicos, servicos,excluir

urlpatterns = [
    path("",servicos, name="servicos"),
    path('agendamento/<int:servico_id>',agendamento,name="agendamento"),
    path("listar_servicos/",listar_servicos,name='listar_servicos'),
    path("criar_servicos/",criar_servicos,name='criar_servicos'),
    path("editar_servicos/<int:servico_id>",editar_servicos,name='editar_servicos'),
    path("excluir/<int:servico_id>",excluir,name='excluir'),
    path("horarios",horarios,name="horarios"),
    path("criar_horario", criar_horario, name="criar_horario"),
    path("editar_horario/<int:horario_id>", editar_horario, name="editar_horario"),
    path("excluir_horario/<int:horario_id>", excluir_horario, name="excluir_horario"), 
    path("agendar",agendar, name="agendar"),
]