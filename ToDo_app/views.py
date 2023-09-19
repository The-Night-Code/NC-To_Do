from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout


# Create your views here.

def Home(request):
    
    
    return render(request,'html/home.html',{"name":"night","username":"nightcode"})
    #return render(request,'html/home.html',{})
    



def LoginU(request):
    
    
    if request.method == "POST":
        
        usernameU =request.POST.get('username')
        passwordU =request.POST.get('password')
        
        user = authenticate(username=usernameU,password=passwordU)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home') 

    #if loginU:
     #   if emailU=="night" :
      #      return HttpResponseRedirect('/home')  
    
    return render(request,'html/login.html')

def SignupU(request):
    
    
    pl=False
    pm=False
    pc=False
    pn=False
    per=False
    if request.method == 'POST':
        username =request.POST.get('username')
        emailU =request.POST.get('email')
        pw1 =request.POST.get('password1')
        pw2 =request.POST.get('password2')
        
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
            data = User.objects.create_user(username=username, email=emailU , password=pw1)
            data.save()
            return render(request, 'html/home.html')

        
    return render(request, 'html/signup.html',{"per":per,"pl":pl,"pm":pm,"pc":pc,"pn":pn})
    
    
    
    
def LogoutU(request):
    logout(request)
    return redirect("/login/")
    #return render(request,'html/login.html')

def TaskList(request):
    
    return render(request,'html/tasklist.html')

def TopPriorities(request):
    
    return render(request,'html/toppriorities.html')

def Reminder(request):
    
    return render(request,'html/reminder.html')

def StickyWall(request):
    
    data={"range":4,
          "sticky_wall_c":[{'id':"a0","title":"title 1111","content":"content 11111"},
                           {'id':"a1","title":"title 222","content":"content 2a123423422"},
                           {'id':"a2","title":"title 333","content":"content 333"},
                           {'id':"a3","title":"title 444","content":"content 444"},
                           {'id':"a4","title":"title 55","content":"content 55"},
                           {'id':"a5","title":"title 666","content":"content 6666"},
                           {'id':"a6","title":"title 777","content":"content 777contcontent 777ent 777content 777content 777content 777content 777content 777"},
                           {'id':"a7","title":"title 888","content":"content 88"},
                           {'id':"a8","title":"title 999","content":"content 99"},
                           {'id':"a9","title":"title 1000","content":"content 1000"},
                           {'id':"a10","title":"title 1111","content":"content 11111"},
                           {'id':"a11","title":"title 1111","content":"content 11111"},
                           {'id':"a12","title":"title 1111","content":"content 11111"},
                           {'id':"a13","title":"title 1111","content":"content 11111"},
                           {'id':"a14","title":"title 1000","content":"content 1000"},
                           {'id':"a15","title":"title 1000","content":"content 123124edgadfg452346sdfg0content 123124edgadfg452346sdfg0content 123124edgadfg452346sdfg0content 123124edgadfg452346sdfg0"}]
          }
    
    
    if request.method == "POST":
        
        s_w_id =request.POST.get('username')
        passwordU =request.POST.get('password')
        
        user = authenticate(username=usernameU,password=passwordU)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home') 

    #if loginU:
     #   if emailU=="night" :
      #      return HttpResponseRedirect('/home')  
    
    return render(request,'html/stickywall.html',data)
  