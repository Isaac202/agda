from django.db import models

class Endereco(models.Model):
    cidade = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    numero = models.IntegerField(blank=True,null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    

