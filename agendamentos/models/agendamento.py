from django.db import models

from .servicos import Servico
from usuarios.models.colaborador import Colaborador
from usuarios.models.clientes import Clientes


STATUS_AGENDAMENTO=(
    ('conf',"CONFIRMADO"),
    ('pen',"PENDENTE"),
    ('agua',"AGUARDANDO",)
)

class Agendamento(models.Model):
     cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
     servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
     colaborador = models.ForeignKey(Colaborador,on_delete=models.CASCADE)
     data = models.DateTimeField()
     comissao = models.CharField(max_length=20)
     valor = models.CharField(max_length=20),
     status = models.CharField(max_length=10,choices=STATUS_AGENDAMENTO)
     
     def __str__(self):
         return f'Agendamento Cliente: {self.cliente}'
     