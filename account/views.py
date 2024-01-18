from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def accHome(request):
    return render(request,"index.html")

def reg(request):
    if request.method=='GET':
        return render(request,"reg.html")
    elif request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('psw')
        return HttpResponse(f"email :{email} \n password :{passwd}")

# def login(request):
#     if request.method == 'GET':
#         return render(request,"login.html")
#     elif request.method == 'POST':
#         username = request.POST.get('uname')
#         passwd = request.POST.get('psw')
#         return HttpResponse(f'username :{username} \n password:{passwd}')
    

#class views
class SignIn(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    def post(self,request):
        username = request.POST.get('uname')
        passwd = request.POST.get('psw')  
        return HttpResponse(f'username:{username} \n password:{passwd}') 

