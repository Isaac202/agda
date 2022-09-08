from usuarios.models.base import Pessoa
from django.db import models


STATUS_COLABORADOR = (
    ('adm',"ADMINISTRATIVO"),
    ('gerente',"GERENTE"),
    ('funcio',"FUNCIONARIO"),
)


class Colaborador(Pessoa):
    tipo_colaborador = models.CharField(
                        max_length=10,
                        choices=STATUS_COLABORADOR,
                        default="funcio"
    )
   
    def __str__(self):
        return self.nome