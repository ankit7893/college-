from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("index page ")
    return render(request , "index.html") 
    

def view_all_stu(request):
    return HttpResponse(" view stu page")


def add_stu(rquest):  
    return HttpResponse("add stu page")


def remove_stu(requerst):
    return HttpResponse("remove page ")


def filter_stu(requerst):
    return HttpResponse("filter page of stu ")


