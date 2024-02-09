from django.db import models

# Create your models here.
class StudentModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100,unique = True)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.firstname

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = "Product"

class TeacherModel(models.Model):
    name = models.CharField(max_length = 100)
    dob = models.DateField()
    email = models.EmailField()
    subject = models.CharField(max_length = 100)