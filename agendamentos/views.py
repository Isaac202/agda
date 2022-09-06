import re
from django.shortcuts import render,redirect
from agendamentos.models.servicos import Servico
# Create your views here.






#==============================VIEWS DE SERVIÇOS=========================#

def servicos(request):
    servico = Servico.objects.all()
    return render(
                request,
                'site/servicos.html',
                {
                    "servico":servico
                }                
                )


def agendamento(request):
    return render(request,"site/agendamento.html")



def listar_servicos(request):
    servico = Servico.objects.all()
    
    if request.GET.get("mensagem"):
        
        mensagem = request.GET["mensagem"]
        
        return render(
                    request,
                    "admin/servicos.html",
                    {
                        "servicos":servico,
                        "mensagem":mensagem,
                    }
                    )
    return render(
                    request,
                    "admin/servicos.html",
                    {
                        "servicos":servico
                    }
                    )

def criar_servicos(request):
    
    if request.method == "POST":
        Servico.objects.create(
            titulo = request.POST["titulo"],
            preco = request.POST["preco"],
            duracao = request.POST["duracao"],
            comissao = request.POST['comissao'],
            descricao = request.POST['descricao'],
            imagen = request.FILES["imagen"],
        )
        print(request.FILES["imagen"])
        return redirect("/listar_servicos?mensagem=success")
    
    return render(
                    request,
                    "admin/criar_servico.html",
        
                    )
    


def editar_servicos(request, servico_id):
    servico =  Servico.objects.filter(id=servico_id)
    print(servico)
    if request.method == "POST":
        servico = servico.update(
            titulo = request.POST["titulo"],
            preco = request.POST["preco"],
            duracao = request.POST["duracao"],
            comissao = request.POST['comissao'],
            descricao = request.POST['descricao'],
            #imagen = request.FILES["imagen"],
        )
        # print(request.FILES["imagen"])
        return redirect("/listar_servicos")
    
    return render(
                    request,
                    "admin/editar_servico.html",
                    {
                        "servico":servico
                    }
        
                    )
    
def excluir(request, servico_id):
    Servico.objects.filter(id=servico_id).delete()
    return redirect("/listar_servicos")

#==============================VIEWS DE SERVIÇOS=========================#