from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from Signup.models import signup

# Create your views here.
def login(request):
    return render(request, 'login.html')

def log(request):
    return HttpResponseRedirect('/login')

def log_in(request):
    if request.method == 'POST':
        user = request.POST['user'].capitalize()
        passy = request.POST['passy']
        verify = auth.authenticate(username=user, password=passy)
        if verify and verify.is_active:
            auth.login(request, verify)
            return render(request, 'user_auth.html')
        else:
            messages.info(request, "Invalid Username or Password")
            return HttpResponseRedirect('login')
    else:
        if request.method == 'GET':
            return render(request, 'user_auth.html')

def get_details(request):
    if request.method == "POST":
        val = request.POST["key"]
        User = get_user_model()
        users = User.objects.all()
        l = []
        for i in users:
            i = str(i).lower()
            if str(val) in i:
                l.append(i)
        content ={
            "users" : l
        }
        return render(request, 'users_list.html', content)

def send_request(request):
    pass

def upload_pic(request, name):
    print(name)
    return render(request, 'user_auth.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
