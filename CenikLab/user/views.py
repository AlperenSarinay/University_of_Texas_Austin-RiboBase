from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .forms import LoginForm,RegisterForm

##Login Page and Register Page backed work is done on this views page.##
# Create your views here.

#database registration of the newly created record
def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username,password=password)
        login(request,new_user)
        return redirect('index')

    return render(request,"register.html",{'form':form})

#code that allows the registered user to enter the system
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():  #Checking if the form is empty
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        login(request,user)
        return redirect("index")     
    return render(request,"login.html",context)

def logoutUser(request):
    return render(request,"logout.html")
