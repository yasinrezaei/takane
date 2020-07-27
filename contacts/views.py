from django.shortcuts import render,redirect
from .models import Contacts
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        takane=request.POST['takane']
        field=request.POST['field']    
        ability=request.POST['ability']
        takane_now=request.POST['takane_now']
        contact=Contacts(name=name,email=email,phone=phone,message=message,user_id=user_id,takane=takane,field=field,ability=ability,takane_now=takane_now)
        contact.save()
        return redirect('home')
