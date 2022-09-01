from django.shortcuts import render

# Create your views here.


def servicos(request):
    return render(request,'site/servicos.html')


def agendamento(request):
    return render(request,"site/agendamento.html")