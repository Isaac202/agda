from usuarios.models.base import Pessoa
from django.db import models


STATUS_CLIENTE = (
    ('lead',"LEAD"),
    ('cliente',"Cliente"),
)

class Clientes(Pessoa):
    status = models.CharField(
                    max_length=10,
                    choices=STATUS_CLIENTE,
                    default="lead"
    )
    
    
    def __str__(self):
        return f'Nome do Cliente {self.nome}'
    

    