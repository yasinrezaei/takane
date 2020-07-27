from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.messages import constants as messages

def register(request):
    if request.method=='POST':
        #get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password'] 
        password2=request.POST['password2']
        #check if password match
        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                #messages.error(request,'That username is taken')
                return redirect('register')
                
            else:
                if User.objects.filter(email=email).exists():
                    #messages.error(request,'That username is taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                     #login after register
                    #auth.login(request,user)
                    #messages.SUCCESS(request,'You are now logged in')
                    #return redirect('index')
                    user.save()
        
                    #messages.SUCCESS(request,'You are now registred and can log in')
                    return redirect('login')
        else:
            return redirect('login')
            #messages.error(request,'Passwords do not match!')
    else:
        return render(request,'Accounts/register.html')









def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #message.SUCCESS(request,'you are know loged in')
            return redirect('dashboard')
        else:
            #messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'Accounts/login.html')
    



def logout(request):
    if request.method=='POST':
        auth.logout(request)
        #messages.SUCCESS(request,'you are now logged out')
        return redirect('home')


def dashboard(request):
    return render(request,'Accounts/dashboard.html')  