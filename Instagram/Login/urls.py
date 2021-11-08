from django.contrib import admin
from django.urls import path
from .views import *
from Signup.views import *
from Instagram_Home.views import *
#from ..Signup.views import signup

urlpatterns = [
    path('', login),
    path('home/', home),
    path('login/', log),
    path('signup/', sign),
    path('log_in', log_in),
    path('logout/', logout),
    path('get_list', get_details),
    path('send_req', send_request),
    path('upload/<str:name>', upload_pic),
    path('upload/logout/', logout),
]
