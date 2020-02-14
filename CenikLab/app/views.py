from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

##Login Page and Register Page backed work is done on this views page.##
# Create your views here.

#database registration of the newly created record
def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username") #Checking if the form is empty
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser = User(email = email)
        newUser.set_password(password)

        newUser.save()  #created newUser
        login(request,newUser)
        

        return redirect("index")
    context =  { 
        "form" : form
    }
    return render(request,"register.html",context)

#code that allows the registered user to enter the system
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():  #Checking if the form is empty
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(email = email,password = password)
        if user is   None:  # If user is empty it won't do anything
            messages.info(request,"Error !!!!!")
            return render(request,"login.html",context) 

        login(request,user)
        return redirect("index")
       
           
    return render(request,"login.html",context)

def logoutUser(request):
    return render(request,"logout.html")
