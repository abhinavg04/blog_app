from django.db import models

# Create your models here.
class StudentModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=100)