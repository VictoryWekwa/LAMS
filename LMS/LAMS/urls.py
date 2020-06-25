import django.contrib.auth.views
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    
path('', views.index, name='home.html')


]
