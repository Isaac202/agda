from django.shortcuts import render

# Create your views here.


def pagamento(request):
    return render(request,'site/pagamento.html')
