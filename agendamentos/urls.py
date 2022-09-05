from django.contrib import admin
from django.urls import path
from agendamentos.views import  agendamento, listar_servicos, servicos

urlpatterns = [
    path("",servicos, name="servicos"),
    path('agendamento/',agendamento,name="agendamento"),
    path("listar_servicos/",listar_servicos,name='listar_servicos')
]