from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from .models import CustomUser, Contact, contentImages
from django.core.mail import send_mail
from .decorators import login_required
import random

# Helper function to generate OTP
def generate_otp():
    return random.randint(100000, 999999)

# Helper function to send OTP via email
def send_otp_via_email(user):
    otp = generate_otp()
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. Use this to log in."
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, email_from, [user.email])
    return otp

# Register view remains unchanged
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if not CustomUser.objects.filter(username=username).exists():
                if not CustomUser.objects.filter(email=email).exists():
                    hashed_password = make_password(password)
                    CustomUser.objects.create(username=username, email=email, password=hashed_password)
                    messages.success(request, 'Registration successful.')
                    return redirect('login')
                else:
                    messages.error(request, 'Email already exists.')
            else:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'register.html')

# Login view with added OTP login functionality
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials.')
            except CustomUser.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Both username and password are required.')

    return render(request, 'login.html')

# OTP Login: Step 1 - Send OTP
def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = CustomUser.objects.get(email=email)
            otp = send_otp_via_email(user)
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            messages.success(request, 'OTP sent to your email.')
            return redirect('verify_otp')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')

    return render(request, 'send_otp.html')

# OTP Login: Step 2 - Verify OTP
def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        otp_sent = request.session.get('otp')
        user_id = request.session.get('user_id')

        if str(otp_entered) == str(otp_sent):
            try:
                user = CustomUser.objects.get(id=user_id)
                request.session['user_id'] = user.id  # Log in the user by setting session
                messages.success(request, 'Login successful.')
                return redirect('home')
            except CustomUser.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Invalid OTP.')

    return render(request, 'verify_otp.html')

# Logout view remains unchanged
@login_required
def logout(request):
    request.session.flush()  # This will remove all session data
    messages.success(request, 'Logged out successfully.')
    return redirect('navbar')

# Other views remain unchanged
@login_required
def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id=user_id)
        context = {'is_authenticated': True, 'user': user}
    else:
        context = {'is_authenticated': False}
    return render(request, 'dashboard.html', context)

@login_required
def movies(request):
    return render(request, 'movies.html')

@login_required
def contact(request):
    data = Contact.objects.all()
    return render(request, 'contact.html', {'datas': data})

def navbar(request):
    return render(request, 'nav.html')

def img(request):
    img = contentImages.objects.last()
    return render(request, 'image.html', {'img': img})
