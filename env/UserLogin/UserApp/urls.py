# accounts/urls.py
# from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('',navbar,name='navbar'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('home/',home, name='home'),  # Simple home view
    path('movies/',movies,name='movies'),
    path('contact/',contact,name='contact'),
    path('img/',img,name='image'),
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]
