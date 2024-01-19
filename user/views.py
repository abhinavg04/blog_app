from django.shortcuts import render
from django.views import View
# Create your views here.

class DashBoardView(View):
    def get(self,request):
        return render(request,"dashboard.html")
    
# def add(request):
#     return render(request,"addition.html")
class AdditionView(View):
    def get(self,request):
        return render(request,"addition.html")