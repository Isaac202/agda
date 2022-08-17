from django.contrib import admin
from agendamentos.models import agendamento,horarios,servicos


admin.site.register(agendamento.Agendamento)
admin.site.register(horarios.Horario)
admin.site.register(servicos.Servico)
