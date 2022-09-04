from django.contrib import admin
from django.urls import path
from pagamentos.views import  pagamento

urlpatterns = [
    path("",pagamento, name="servicos"),
    #path('pagamento/',agendamento,name="agendamento")
]