from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .form import BlogForm,StudentDetails,ProductForm,SubForm
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
        return render(request,"multiplication.html")
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
    
class AddBlog(View):
    def get(self,request):
        form = BlogForm()
        return render(request,"add_blog.html",{"form":form})
    def post(self,request):
        # title = request.POST.get('title')
        # body = request.POST.get('body')
        # auth = request.POST.get('author')
        # img  = request.POST.get('image')
        # print(title,body,auth,img)
        form_data = BlogForm(data=request.POST,files=request.FILES)
        print(form_data.is_valid())
        if form_data.is_valid():
            title = form_data.cleaned_data.get('title')
            body = form_data.cleaned_data.get('body')
            auth = form_data.cleaned_data.get('author')
            print(title,body,auth)
            return HttpResponse("SuccessFull")
        else:
            print(form_data.errors)
            return HttpResponse("Submission Failed")
        
class AddStud(View):
    def get(self,request):
        stud_form = StudentDetails()
        return render(request,"add_student.html",{"form":stud_form})
    def post(self,request):
        form_data = StudentDetails(data=request.POST)
        print(form_data.is_valid())
        if form_data.is_valid():
            firstname = form_data.cleaned_data.get('firstname')
            lastname = form_data.cleaned_data.get('lastname')
            dob = form_data.cleaned_data.get('dob')
            email = form_data.cleaned_data.get('email')
            phone = form_data.cleaned_data.get('phone')
            address = form_data.cleaned_data.get('address')
            department = form_data.cleaned_data.get('department')
            print(firstname,lastname,dob,email,phone,address,department)
            return HttpResponse("SuccessFully Submitted")
        else:
            print(form_data.errors)
            return HttpResponse("Submission Failed")


class ProductView(View):
    def get(self,request):
        pr_form = ProductForm()
        return render(request,"product.html",{"form":pr_form})
    def post(self,request):
        form_data = ProductForm(data=request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            return HttpResponse("post hit")
        else:
            print(form_data.errors)
            return render(request,"product.html",{"form":form_data})
    

class SubView(View):
    def get(self,request):
        sub_form = SubForm()
        return render(request,"subtraction.html",{"form":sub_form})
    def post(self,request):
        form_data = SubForm(data=request.POST)
        if form_data.is_valid():
            num1 = form_data.cleaned_data.get('num1')
            num2 = form_data.cleaned_data.get('num2')
            diff = int(num1)-int(num2)
            context={}
            context["data"] = diff
            return render(request,'subtraction.html',context)
        else:
            print(form_data.errors)
            return render(request,"subtraction.html",{"form":form_data})    
    