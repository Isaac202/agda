from django.contrib import admin
from usuarios.models import clientes,colaborador
# Register your models here.


admin.site.register(clientes.Clientes)
admin.site.register(colaborador.Colaborador)