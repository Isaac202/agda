from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from agendamentos.models.agendamento import Agendamento
# Create your views here.

@csrf_exempt
def pagamento(request):
    agendamento = Agendamento.objects.get(id=request.GET.get("age"))
    return render(
            request,
            'site/pagamento.html',
            {
                "agenda":agendamento
            }
            )
@csrf_exempt
def pagar(request):
    if request.method == "POST":
        agendamento_id = Agendamento.objects.filter(id= request.POST["agenda"])
        agendamento_id.update(
            status = "conf"
        )
        print(request.POST)
    return ""
