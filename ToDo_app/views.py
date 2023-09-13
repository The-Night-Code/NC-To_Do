from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'html/home.html')
    #return render(request,'html/home.html',{})