"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

#laying pipelines:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('removepunc', views.removepunc, name='rempunc'),    #127.0.0.1:8000/removepunc
    path('capitalizefirst', views.capfirst, name='capfirst'),  # 127.0.0.1:8000/capitalizefirst
    path('newlineremove', views.newlineremove, name='newlineremove'),  #127.0.0.1:8000/newlineremove
    path('spaceremove', views.spaceremove, name='spaceremove'),  #127.0.0.1:8000/spaceremove
    path('charcount', views.charcount, name='charcount')   #127.0.0.1:8000/charcount
]
