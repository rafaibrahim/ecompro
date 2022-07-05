from django.shortcuts import render
from django.http import HttpResponse

def fun(request):
    return HttpResponse("hiii")

def index(request):
    return render(request, 'users/index.html')

def new(request):
    return render(request, 'users/new.html')

def master(request):
    return render(request, 'users/master.html')