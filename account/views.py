from django.shortcuts import render

# Create your views here.
def accHome(request):
    return render(request,"index.html")

def reg(request):
    return render(request,"reg.html")

def login(request):
    return render(request,"login.html")
