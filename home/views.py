
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# from djanipware import get_client_ip
# from ipware import get_ip_address_from_request

# Create your views here.
def home(req):

    

    
    return render(req, 'home.html')



# Sign in function
def signin(req):
    message = {

    }
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('dashboard')
        else:
            m1 = messages.error(req, username + "  mavjud emas ! ")
            message['m1'] = message
    return render(req, 'signin.html')


# Log Out function
def LogOut(request):
    logout(request)
    return redirect('signin')



# Sign up function
def signup(req):
    message = {

    }
    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            m = messages.error(req, first_name + " uchun account yaratildi!")
            message['m1'] = message
            return redirect('signin')


        else:
            m1 = messages.error(req, "Siz formani noto`g`ri to`ldirdingiz!")
            message['m1'] = message
            print(messages.error)

    return render(req, 'signup.html')




# User dashboard function
def user_dashboard(req):
    # ip = get_client_ip(req)
    return render(req, 'user_dashboard.html')



# Error pages start 
def error_404_view(req, exception):
    try:
        client_address = req.META['HTTP_X_FORWARDED_FOR']
        print(client_address)
    except:
# case localhost ou 127.0.0.1
        client_address = req.META['REMOTE_ADDR']
        print(client_address)
    data = {"name": client_address}
    return render(req,'error_404.html', data)

def error_500_view(request, *args, **argv):
    return render(request, 'error_500.html', status=500)

def error_400_view(req, exception):

    return render(req, 'error_400.html')

def error_403_view(req, exception):

    return render(req, 'error_403.html')
# Error pages end




# User Profile page 
def profile(req):

    return render(req, 'profile.html')

    
# Auth with social 

def Auth_google(req):
# http://127.0.0.1:8000/accounts/google/login/?process=login

    return redirect('google/login/?process=login')

def Auth_github(req):
# http://127.0.0.1:8000/accounts/github/login/?process=login
    return redirect('github/login/?process=login')



