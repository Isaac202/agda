from django.contrib import admin
from django.urls import path
from pagamentos.views import  pagamento, pagar

urlpatterns = [
    path("",pagamento, name="servicos"),
    path("pagar", pagar,name="pagar")
    #path('pagamento/',agendamento,name="agendamento")
]