from django.contrib import admin
from django.urls import path
from base.views import  entrar

urlpatterns = [
    path("",entrar, name="entrar"),
]
