from django.shortcuts import render,redirect
from usuarios.models.clientes import Clientes
from django.contrib.auth.models import User

# Create your views here.


def cadastrar_cliente(request):
    if request.method == "POST":
        user = User.objects.create(
            username = request.POST["email"],
            email=request.POST["email"])
        user.set_password(request.POST["senha1"])
        Clientes.objects.create(
            nome = request.POST["nome"],
            user = user,
            email =request.POST["email"],
            telefone = request.POST["whapp"]
        )
        return redirect("login")
    return render(request,'site/cadastro.html')