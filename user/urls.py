from django.urls import path
from user.views import *
urlpatterns = [
    path('',DashBoardView.as_view(),name="dash"),
    path('add',AdditionView.as_view(),name="add"),
    path('mul',MulView.as_view(),name="mul"),
    path('word',WordCount.as_view(),name="word"),
]
