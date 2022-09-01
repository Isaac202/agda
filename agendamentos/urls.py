from django.contrib import admin
from django.urls import path
from agendamentos.views import  servicos

urlpatterns = [
    path("",servicos, name="servicos"),
]