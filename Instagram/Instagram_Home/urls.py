"""Instagram_Home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_render),
    path('/', home_render),
    path('login/', include('Login.urls')),
    path('signup/', include('Signup.urls')),
    path('get_list/', include('Login.urls')),
    path('send_req/', include('Login.urls')),
    path('upload/<str:name>', include('Login.urls')),
    #path('upload/logout', include('Login.urls')),
    #path('logout/', include())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
