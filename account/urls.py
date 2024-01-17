from django.urls import path
from .views import reg
urlpatterns = [
    path('reg',reg,name="reg_form"),
    path('login',reg,name="reg_form"),
]
