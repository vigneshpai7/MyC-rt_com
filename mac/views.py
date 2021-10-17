from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def mainPage(request):
    return render(request,"index.html")


# login and sing up


def handlesingup(request):
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # adding checks
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')

        # create the user
        newuser=User.objects.create_user(username,email,pass1)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        messages.success(request,"your account is created")
        return redirect("/")

    else:
        return HttpResponse("Error 404")  
        # login and log out  
def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/shop")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")
    return HttpResponse("404- Not found")
   
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')