from django.shortcuts import render,redirect
from usuarios.models.clientes import Clientes
from django.contrib.auth.models import User
from django.http import JsonResponse
from base.utils import validar_usuario
from django.views.decorators.csrf import csrf_exempt
from usuarios.models.colaborador import Colaborador

# Create your views here.

@csrf_exempt
def cadastrar_cliente(request):
    if request.method == "POST":
        print(request.POST)
        mensagem_error = validar_usuario(
            request.POST["email"],
            request.POST["senha1"],
            request.POST["senha2"])
        print("mensagem_error",mensagem_error)
        if mensagem_error:
            return JsonResponse(mensagem_error)
            # return render(request,'site/cadastro.html',mensagem_error)
        user = User.objects.create_user(
            username = request.POST["email"],
            email=request.POST["email"],
            password=request.POST["senha1"]
            )
        Clientes.objects.create(
            nome = request.POST["nome"],
            user = user,
            email =request.POST["email"],
            telefone = request.POST["whapp"]
        )
        return JsonResponse({"sucesso":"true"})
    return render(request,'site/cadastro.html')

def clientes(request):
    clientes = Clientes.objects.all()
    
    return render(
                request,
                "admin/clientes.html",
                {
                    "clientes":clientes
                }
                )


def funcionarios(request):
    funcionario = Colaborador.objects.all()
    print(funcionario.values())
    return render(
                request,
                "admin/funcionario.html",
                {
                    "funcionarios":funcionario
                }
                )
    

def criar_funcionarios(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username = request.POST["email"],
            email=request.POST["email"],
            password=request.POST["senha1"]
            )
        
        print(request.POST["tipo"])
        Colaborador.objects.create(
            nome = request.POST["nome"],
            user = user,
            email =request.POST["email"],
            telefone = request.POST["whapp"],
            tipo_colaborador = request.POST["tipo"]
        )
        return redirect("funcionarios")
    return render(
                request,
                "admin/criar_funcionarios.html",
                )
    

def editar_funcionarios(request, funcionario_id):
    funcionario = Colaborador.objects.filter(id=funcionario_id)
    usuario_do_funcionario = list(funcionario.values_list("user",flat=True))[0]
    user = User.objects.filter(id=usuario_do_funcionario)
    print(user)
    if request.method == "POST":
        print("passou aqui")
        user.update(
            username = request.POST["email"],
            email=request.POST["email"]
        )
        # user.set_password(request.POST["senha1"])
        
        print(request.POST["tipo"])
        funcionario.update(
            nome = request.POST["nome"],
            email =request.POST["email"],
            telefone = request.POST["whapp"],
            tipo_colaborador = request.POST["tipo"]
        )
        return redirect("funcionarios")
    return render(
                request,
                "admin/editar_funcionario.html",
                {
                    "funcionario":funcionario
                }
                )
    
    
def excluir_funcionarios(request, funcionario_id):
    funcionario = Colaborador.objects.filter(id=funcionario_id)
    funcionario.delete()
    return redirect("funcionarios")
    