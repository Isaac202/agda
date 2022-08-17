from django.db import models



class Servico(models.Model):
    titulo = models.CharField(max_length=255, blank=True)
    preco = models.CharField(max_length=20,blank=True,null=True)
    duracao = models.CharField(max_length=20, blank=True, null=True)
    comissao = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='media/imagens/%d/%m/%Y/',null=True, blank=True)
