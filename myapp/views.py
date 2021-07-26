from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Views functions

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if username == '' or email == '' or password == '' or password_confirm == '':
            messages.error(request, 'Please enter all the fields')
            return redirect('register')
        
        else:

            if password == password_confirm:

                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('register')

                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists')
                    return redirect('register')
                
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        
            else:
                messages.info(request, 'Passwords do not match')
                return redirect('register')
   
    else:
        return render(request, 'register.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})