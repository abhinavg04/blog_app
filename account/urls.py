from django.urls import path
from .views import reg,SignIn
urlpatterns = [
    path('reg',reg,name="reg_form"),
    path('login',SignIn.as_view(),name="login"),
]
