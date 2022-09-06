from django.shortcuts import render

# Create your views here.


def manager(request):
    return render(request,"admin/index.html")