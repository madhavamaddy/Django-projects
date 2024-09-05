import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

def send_otp_via_email(email):
    otp = generate_otp()
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. Please use this to verify your account."
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, email_from, [email])

    return otp  # Return the OTP for verification purposes
