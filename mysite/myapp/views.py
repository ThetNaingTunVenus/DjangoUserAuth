from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import *
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password invalid')
            # return render(request, 'login.html', context)
        context ={}
        return render(request, 'login.html', context)
    

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'User Created Successful')
            return redirect('login')
    context ={'form':form}
    return render(request, 'register.html', context)



@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')