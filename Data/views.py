from os import pread
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return render(request,"Data/home.html")



def home(request):
    users = User.objects.all()
    silver = User.objects.get(username = 'silver')

    return render(request,'Data/index.html',{
        "users":users,
        "silver":silver
    })


def profile(request,id):
    tasks = Tasks.objects.filter(user = id )
    user = User.objects.get(id=id)
    silver = User.objects.get(username = 'silver')
    if request.method == "POST":
        data = request.POST.copy()
        data['user'] = user.id
        form = AddTask(data)
        if form.is_valid():
            form.save()
            return redirect('profile',id=id)
        else:
           return redirect("home")
       
       


    return render(request,'Data/profile.html',{
        "tasks":tasks,
        "user":user,
        "silver":silver
    })

def delete_item(request, id):
    item = get_object_or_404(Tasks, id=id)
    pk = item.user.id
    item.delete()
    return redirect('profile',id=pk)
  # Redirect to a relevant view


def edit_task(request,id):
    item = Tasks.objects.get(id=id)
    form = AddTask(instance=item)
    data = request.POST.copy()
    data['user'] = item.user.id
    if request.method == 'POST':
      form = AddTask(data,instance=item)
      if form.is_valid():
         form.save()
         return redirect('profile',item.user.id)
    return render(request,'Data/edit.html',{
        "form":form
    })
      
          


    

    
    
    