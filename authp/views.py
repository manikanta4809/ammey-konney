from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Use
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse

def home(request):
	return render (request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            x=authenticate(request,username=username,password=password)
            if x is not None:
                login(request, x )

            Up=Use(username=username,password=password)
            Up.save()

            messages.success(request,f"hola {username}, account created successfully let's get started by logging in!")
            return redirect ('thome')
    else:
            form=UserRegisterForm()
    
    return render(request,'register.html',{'form':form}, )

@login_required()

def profile(request):
    return render(request, 'profile.html')