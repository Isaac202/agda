from django.http import JsonResponse
from django.shortcuts import render,redirect
from agendamentos.models.horarios import Horario
from agendamentos.models.servicos import Servico
from usuarios.models.colaborador import Colaborador
import calendar 
from datetime import date, datetime
from agendamentos.forms import HorarioForm
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


def agendamento(request,servico_id):
    servico = Servico.objects.filter(id=servico_id)
    horarios_disponiveis_do_servico = Horario.objects.filter(servico=servico_id).filter(disponivel=True)
    dia_hoje = datetime.today()
    print(dia_hoje)
    ano = dia_hoje.year 
    mes = dia_hoje.month 
    dias = calendar.monthrange(ano,mes) 
    lista_dias = datetime(ano,mes,dias[1])
    print(dia_hoje.day)
    numero_de_dias =lista_dias.day 
    print(numero_de_dias)
    semana = date(year=ano, month=mes, day=dia_hoje.day)
    dias_para_adcionar = numero_de_dias - dia_hoje.day
    print(dias_para_adcionar)
    DIAS = [
        'Seg',
        'Ter',
        'Qua',
        'Qui',
        'Sex',
        'Sáb',
        'Dom'
    ]
    dia = []
    semana = []
    for dia_semana in range(dias_para_adcionar+1):
        dia_add =numero_de_dias-dias_para_adcionar
        indice_semana = date(year=ano, month=mes, day=dia_add).weekday()
        dia.append({
                    "dia":dia_add,
                    "semana":DIAS[indice_semana]
                    })
        dias_para_adcionar =dias_para_adcionar -1
    
    return render(
            request,"site/agendamento.html",
            {
                "semana_dia":dia
            }
            )

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



def horarios(request):
    horarios = Horario.objects.all()
    print(horarios)
    return render(
                request,
                "admin/agendas.html",
                {
                    "horarios":horarios
                }
                )

def criar_horario(request):
    
    form = HorarioForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect("/horarios")
    print(request.POST)
    return render(
                request,
                "admin/criar_agenda.html",
                {
                    "form":form,
                }
                )
    

def editar_horario(request,horario_id):
    horario = Horario.objects.get(id=horario_id)
    form = HorarioForm(instance=horario)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/horarios")
    print(request.POST)
    return render(
                request,
                "admin/criar_agenda.html",
                {
                    "form":form,
                }
                )
    
def excluir_horario(request,horario_id):
    horario = Horario.objects.filter(id=horario_id)
    horario.delete()
    return redirect("/horarios")  