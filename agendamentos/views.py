from django.shortcuts import render
from agendamentos.models.servicos import Servico
# Create your views here.






#==============================VIEWS DE SERVIÇOS=========================#

def servicos(request):
    return render(request,'site/servicos.html')


def agendamento(request):
    return render(request,"site/agendamento.html")



def listar_servicos(request):
    servico = Servico.objects.all()
    return render(
                    request,
                    "admin/schedule/listar_servico.html",
                    {
                        "servicos":servico
                    }
                    )

def criar_servicos(request):
    pass

#==============================VIEWS DE SERVIÇOS=========================#