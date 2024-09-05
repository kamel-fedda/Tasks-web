from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return render(request,'users/error.html',{
                "error":"We didn't find the user"
            }) 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("profile",user.id)
        else:
            return render(request,"users/error.html",{
                "error":"Some thing went wrong"
            })
                




    return render(request,"users/index.html")


def signin(request):
    form = UserCreationForm() 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request,user)
            return redirect("profile",user.id)
        else:
            return render(request,"users/error.html",{"error":"ERROR 404"})
        
    return render(request,"users/signin.html",{
        "form":form
        })


def logoutUser(request):
    logout(request)
    return redirect("index")