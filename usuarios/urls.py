from django.contrib import admin
from django.urls import path
from usuarios.views import cadastrar_cliente

urlpatterns = [
    path("cadastrar_cliente",cadastrar_cliente, name="cadastrar_cliente"),
]