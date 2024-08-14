"""
URL configuration for MyDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from MyDjango_App import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_view, name='form'),
    path('webpage/', views.web_page_view, name='webpage'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('booking/', views.booking, name='booking'),
    # path('events/', views.events, name='events'),

]

