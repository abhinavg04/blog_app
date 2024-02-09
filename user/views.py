from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .form import BlogForm,StudentForm,ProductForm,SubForm,TeacherModelForm
from .models import StudentModel,ProductModel,TeacherModel
from django.http import Http404
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
        stud_form = StudentForm()
        return render(request,"add_student.html",{"form":stud_form})
    def post(self,request):
        form_data = StudentForm(data=request.POST)
        if form_data.is_valid():
            firstname = form_data.cleaned_data.get('firstname')
            lastname = form_data.cleaned_data.get('lastname')
            dob = form_data.cleaned_data.get('dob')
            email = form_data.cleaned_data.get('email')
            phone = form_data.cleaned_data.get('phone')
            address = form_data.cleaned_data.get('address')
            department = form_data.cleaned_data.get('department')
            try:
                st = StudentModel(
                    firstname=firstname,lastname=lastname,dob=dob,
                    email=email,phone=phone,address=address,department=department)
                st.save()
            except:
                raise Http404("some error occured")
            return redirect("stud_list")
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
            title = form_data.cleaned_data.get('title')
            description = form_data.cleaned_data.get('description')
            type = form_data.cleaned_data.get('type')
            price = form_data.cleaned_data.get('price')
            prodmodel = ProductModel(title=title,description=description,type=type,price=price)
            prodmodel.save()
            return redirect("prod_list")
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
    
class StudentListView(View):
    def get(self,request):
        students = StudentModel.objects.all()
        print(students)
        return render(request,"students_list.html",{"data":students})
    
class ProductListView(View):
    def get(self,request):
        products = ProductModel.objects.all()
        return render(request,"product_list.html",{"data":products})
    
class StudentDetails(View):
    def get(self,request,**kwargs):
        id = kwargs.get('pk')
        stud = StudentModel.objects.get(pk = id)
        return render(request,"student_details.html",{"data":stud})
    
class StudentDelete(View):
    def get(self,request,**kwargs):
        id = kwargs.get('id')
        stud = StudentModel.objects.get(id = id)
        stud.delete()
        return redirect("stud_list")
    
def prodDelete(request,id):
    prod = ProductModel.objects.get(id = id)
    prod.delete()
    return redirect("prod_list")

class StudEdit(View):
    def get(self,request,id):
        studmodel = StudentModel.objects.get(id=id)
        stud = StudentForm(initial={"firstname":studmodel.firstname,"lastname":studmodel.lastname,"dob":studmodel.dob,"email":studmodel.email,"phone":studmodel.phone,"address":studmodel.address,"department":studmodel.department})
        return render(request,"studentedit.html",{"form":stud})
    def post(self,request,id):
        form_data = StudentForm(data=request.POST)
        studmodel = StudentModel.objects.get(id=id)
        if form_data.is_valid():
            studmodel.firstname = form_data.cleaned_data.get('firstname')
            studmodel.lastname = form_data.cleaned_data.get('lastname')
            studmodel.dob = form_data.cleaned_data.get('dob')
            studmodel.email = form_data.cleaned_data.get('email')
            studmodel.phone = form_data.cleaned_data.get('phone')
            studmodel.address = form_data.cleaned_data.get('address')
            studmodel.department = form_data.cleaned_data.get('department')
            studmodel.save()
            return redirect("stud_list")
        else:
            return render(request,'student_list.html',{"form":form_data})
        
class ProdEdit(View):
    def get(self,request,**kwargs):
        id = kwargs.get('id')
        prodmodel = ProductModel.objects.get(id=id)
        prod = ProductForm(initial={"title":prodmodel.title,"description":prodmodel.description,"type":prodmodel.type,"price":prodmodel.price})
        return render(request,"productedit.html",{"form":prod})
    def post(self,request,**kwargs):
        id = kwargs.get('id')
        form_data = ProductForm(data=request.POST)
        Prodmodel = ProductModel.objects.get(id=id)
        if form_data.is_valid():
            Prodmodel.title = form_data.cleaned_data.get('title')
            Prodmodel.description = form_data.cleaned_data.get('description')
            Prodmodel.type = form_data.cleaned_data.get('type')
            Prodmodel.price = form_data.cleaned_data.get('price')
            Prodmodel.save()
            return redirect("prod_list")
        else:
            return render(request,'student_list.html',{"form":form_data})
        
class Addteacher(View):
    def get(self,request):
        form = TeacherModelForm()
        return render(request,"add_teacher.html",{"form":form})
    def post(self,request):
        form = TeacherModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Teacher details saved')
        else:
            return render(request,'add_teacher.html',{'form':form})

def teachListView(request):
    model = TeacherModel.objects.all()
    print(model)
    return render(request,'teacher_list.html',{"data":model})
def teachDelete(request,id):
    data = TeacherModel.objects.get(id=id)
    data.delete()
    return redirect('viewteach')
class TeacherEditView(View):
    def get(self,request,id):
        teachmodel = TeacherModel.objects.get(id=id)
        form = TeacherModelForm(instance=teachmodel)
        return render(request,'edit_teacher.html',{'form':form})