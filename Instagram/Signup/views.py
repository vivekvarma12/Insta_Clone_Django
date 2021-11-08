from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
from .models import signup

def signupi(request):
    return render(request, 'signup.html')
def sign(request):
    return HttpResponseRedirect('/signup')

def signup_store(request):
    if request.method == "POST":
        user_name = request.POST['user'].capitalize()
        email = request.POST['email']
        passy = request.POST['pass1']
        if (not User.objects.filter(username=user_name).exists()) and (not User.objects.filter(email=email).exists()):
            obj = User.objects.create_user(username=user_name, email=email, password=passy)
            obj.save()
            messages.info(request, 'Successfully Registered!!')
            return HttpResponseRedirect('/login')
        else:
            print(user_name, email, passy)
            messages.info(request, 'Username/Email already exists')
            return HttpResponseRedirect('/signup')


