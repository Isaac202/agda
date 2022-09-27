from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.

def entrar(request): 
    if request.method == "POST":
        user = User.objects.get(username=request.POST['usuario'])
        if user:
            usuario = authenticate(username=user.username,
                                password=request.POST["senha"])
            if usuario:
                login(request,usuario)
                return redirect("/")
            else:
                return render(request,"login/index.html",
                              {
                                  "mensagem":"E-mail ou senha incorretos, por favor, tente novamente, ou então tente recuperar sua conta",
                                  "color":"red"
                               })
    return render(request,"login/index.html")
    