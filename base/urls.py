from django.contrib import admin
from django.urls import path
from base.views import  login

urlpatterns = [
    path("",login, name="login"),
]
