from django.contrib import admin
from django.urls import path
from agendamentos.views import  agendamento, servicos

urlpatterns = [
    path("",servicos, name="servicos"),
    path('agendamento/',agendamento,name="agendamento")
]