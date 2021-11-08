from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

def home_render(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponseRedirect('/')