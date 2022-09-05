from django.shortcuts import render

# Create your views here.


def manager(request):
    return render(request,"admin/home/index.html")