from django.db import models
from .servicos import Servico
from usuarios.models.colaborador import Colaborador


class DiaSemana(models.Model):
    segunda = models.BooleanField(default=True)
    terca = models.BooleanField(default=True)
    quarta = models.BooleanField(default=True)
    quinta = models.BooleanField(default=True)
    sexta = models.BooleanField(default=True)
    sabado = models.BooleanField(default=True)
    domingo = models.BooleanField(default=True)
class Horario(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    inicio = models.TimeField()
    fim = models.TimeField()
    dia_da_semana = models.ManyToManyField(DiaSemana)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    