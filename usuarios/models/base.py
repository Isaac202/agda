from django.db import models
from django.contrib.auth.models import User
from cadastro.models.endereco import Endereco


class Pessoa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=True,null=True)
    telefone = models.CharField(max_length=25,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    imagem = models.ImageField(upload_to='media/imagens/%d/%m/%Y/',null=True, blank=True)
    cpf = models.CharField(max_length=25, blank=True, null=True)
    rg = models.CharField(max_length=20,blank=True,null=True)
    endereco = models.ForeignKey(
                    Endereco,on_delete=models.CASCADE,
                    blank=True, null=True
                    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract=True