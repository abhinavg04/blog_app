from django.urls import path
from user.views import *
urlpatterns = [
    path('',DashBoardView.as_view(),name="dash"),
    path('add',AdditionView.as_view(),name="add"),
    path('mul',MulView.as_view(),name="mul"),
    path('word',WordCount.as_view(),name="word"),
    path('blog',AddBlog.as_view(),name="blog"),
    path('addstud',AddStud.as_view(),name="add_stud"),
    path('product',ProductView.as_view(),name="prod"),
    path('sub',SubView.as_view(),name="sub"),
    path('stud_list',StudentListView.as_view(),name="stud_list"),
    path('prod_list',ProductListView.as_view(),name="prod_list"),
    path('prod_list/<int:id>',prodDelete,name="prod_delete"),
    path('stud_list/<int:pk>',StudentDetails.as_view(),name="s_details"),
    path('stud_delete/<int:id>',StudentDelete.as_view(),name="s_delete"),
    path('stud_edit/<int:id>',StudEdit.as_view(),name="studEdit"),
    path('prod_edit/<int:id>',ProdEdit.as_view(),name="prodEdit"),
    path('addteach',Addteacher.as_view(),name="addteach"),
    path('viewteach',teachListView,name="viewteach"),
    path('viewteach/<int:id>',teachDelete,name="t_delete"),
    path('viewteach/edit/<int:id>',TeacherEditView.as_view(),name="t_edit"),
]
