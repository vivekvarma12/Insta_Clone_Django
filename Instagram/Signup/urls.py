from django.contrib import admin
from django.urls import path
from .views import *
from Login.views import *
from Instagram_Home.views import *

urlpatterns = [
    path('', signupi),
    path('home/', home),
    path('signup/', sign),
    path('signup_store', signup_store),
    path('login/', log),
]