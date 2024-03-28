from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest
from django.http import JsonResponse
from .models import FingerPrint
from .utils import generate_fingerprint

# Create your views heref.


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm password')
        # Generate fingerprint and store
        fingerprint = generate_fingerprint(request)
        if password1!=password2:
            messages.error(request,'passwords didnot match ')
            return redirect('../signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('../signup')
        else:
            try:
                FingerPrint.objects.get(fingerprint=fingerprint)
                messages.error(request, 'Someone has already registered with this device.')
                return redirect('../signup')
            except FingerPrint.DoesNotExist:
                user = User.objects.create_user(username, email, password1)
                user.save()
                fingerprint_instance = FingerPrint()
                fingerprint_instance.username = user
                fingerprint_instance.fingerprint = fingerprint
                fingerprint_instance.save()
                messages.success(request, 'Successfully registered.')
                return redirect('../login')      

    else:
        return render(request,'Accounts/signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        fingerprint = generate_fingerprint(request)
        print(username)
        print(password)
        # Authenticate the user
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if FingerPrint.objects.filter(username=user, fingerprint=fingerprint).exists():
                login(request, user)
                messages.success(request, 'Successfully logged in')
                return redirect('index')
            else:
                messages.error(request, 'Your device is not recognized. Please log in from a recognized device.')
                return redirect('login')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        # Method Not Allowed for non-POST requests
        return render(request, 'Accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')


