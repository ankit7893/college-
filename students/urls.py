from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path("" , views.index , name = "index"),
    path("view_all_stu" , views.view_all_stu , name = "view_all_stu"),
    path("add_stu" , views.add_stu , name = "add_stu"),
    path("remove_stu" , views.remove_stu , name = "remove_stu"),
    path("filter_stu" , views.filter_stu , name = "filter_stu"),
]



