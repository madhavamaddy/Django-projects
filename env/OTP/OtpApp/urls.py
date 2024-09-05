from django.urls import path
from .views import send_otp_view, verify_otp_view,index

urlpatterns = [
    path('send-otp/', send_otp_view, name='send_otp'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    path('',index,name='home')
]
