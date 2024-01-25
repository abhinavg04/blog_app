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