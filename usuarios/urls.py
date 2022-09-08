from django.contrib import admin
from django.urls import path
from usuarios.views import cadastrar_cliente, clientes, criar_funcionarios, editar_funcionarios, excluir_funcionarios, funcionarios

urlpatterns = [
    path("cadastrar_cliente",cadastrar_cliente, name="cadastrar_cliente"),
    path("clientes",clientes, name="clientes"),
    path("funcionarios",funcionarios,name="funcionarios"),
    path("criar_funcionarios",criar_funcionarios,name="criar_funcionarios"),
    path("editar_funcionario/<int:funcionario_id>",editar_funcionarios, name="editar_funcionario"),
    path("excluir_funcionarios/<int:funcionario_id>",excluir_funcionarios, name="excluir_funcionario")
]

