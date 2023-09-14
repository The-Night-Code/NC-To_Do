from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def Home(request):
    return render(request,'html/home.html')
    #return render(request,'html/home.html',{})
    
def Login(request):
    lo =request.POST.get('login')
    print(lo)
    if lo:

        return HttpResponseRedirect('/home')  
     
    return render(request,'html/login.html')