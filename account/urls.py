from django.urls import path
from .views import reg,login
urlpatterns = [
    path('reg',reg,name="reg_form"),
    path('login',login,name="login"),
]
