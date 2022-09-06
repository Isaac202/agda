from django.contrib import admin
from django.urls import path
from maneger.views import  manager

urlpatterns = [
    path("",manager, name="maneger"),
    #path('pagamento/',agendamento,name="agendamento")
]