from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
# Create your views here.

class DashBoardView(View):
    def get(self,request):
        return render(request,"dashboard.html")
    
# def add(request):
#     return render(request,"addition.html")
class AdditionView(View):
    def get(self,request):
        return render(request,"addition.html")
    def post(self,request):
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        try:
            sum = int(num1)+int(num2)
        except:
            sum = "error"
        context={}
        context["data"] = sum
        return render(request,'addition.html',context)
class MulView(View):
    def get(self,request):
        return render(request,"addition.html")
    def post(self,request):
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        try:
            sum = int(num1)*int(num2)
        except:
            sum = "error"
        context={}
        context["data"] = sum
        return render(request,'multiplication.html',context)
class WordCount(View):
    def get(self,request):
        return render(request,"word_count.html")
    def post(self,request):
        sentence = request.POST.get('text')
        word_list = sentence.split(" ")
        d = {}
        for word in word_list:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        context={}
        context["data"] = d
        return render(request,'word_count.html',context)
