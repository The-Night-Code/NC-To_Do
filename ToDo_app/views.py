from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Home(request):
    return render(request,'html/home.html')
    #return render(request,'html/home.html',{})
    
def Login(request):
    loginU =request.POST.get('login')
    emailU =request.POST.get('email')
    passwordU =request.POST.get('password')

    if loginU:
        if emailU=="night" :
            return HttpResponseRedirect('/home')  
     
    return render(request,'html/login.html')

def Signup(request):

    emailU =request.POST.get('email')
    pw1 =request.POST.get('password1')
    pw2 =request.POST.get('password2')
    
    pl=False
    pm=False
    pc=False
    pn=False
    per=False
    if request.method == 'POST':
        per = True
        
        
    if str(pw1) == str(pw2):
        pm=True
        for i in str(pw1):
            # if string has letter
            if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                pc = True
            # if string has number
            if i in "0123456789":
                pn = True

    
    if len(str(pw1)) >= 8 :
        pl=True
        
   
    if pl and pm and pc and pn :
        return render(request, 'html/home.html')
    else:
        return render(request, 'html/signup.html',{"per":per,"pl":pl,"pm":pm,"pc":pc,"pn":pn})
    
    
    
    
    