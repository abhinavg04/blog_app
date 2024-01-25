from typing import Any
from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=500)
    author = forms.CharField(max_length=100)
    image = forms.FileField()

class StudentDetails(forms.Form):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your First name"}))
    lastname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your last name"}))
    dob = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","placeholder":"Enter your date of birth"}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter your phone number"}))
    address = forms.CharField(max_length=200,widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Enter your address"}))
    department = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your department"}))

class ProductForm(forms.Form):
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    type = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        price = cleaned_data.get("price")
        if len(title)<3:
            self.add_error("title","title must be atleast 3 characters")
        if price<0:
            self.add_error("price","price must be a positive value")
        print(title,price)
        return cleaned_data
    
class SubForm(forms.Form):
    num1 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control m-2"}))
    num2 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control m-2 "}))

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        num1 = cleaned_data.get("num1")
        num2 = cleaned_data.get("num2")
        if num1 < num2:
            self.add_error("num1","number 1 should be greater than number 2")
        return cleaned_data