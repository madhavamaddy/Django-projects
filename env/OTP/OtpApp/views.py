from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .utils import send_otp_via_email  # Assuming utils.py contains the function
# from django.http import JsonResponse
@require_POST
def send_otp_view(request):
    email = request.POST.get('email')

    if email:
        otp = send_otp_via_email(email)
        # Store OTP in session or database for validation
        request.session['otp'] = otp
        return JsonResponse({'message': 'OTP sent successfully!'})
    else:
        return JsonResponse({'error': 'Email is required'}, status=400)



def verify_otp_view(request):
    otp_entered = request.POST.get('otp')

    if otp_entered and str(otp_entered) == str(request.session.get('otp')):
        # OTP verified successfully
        return JsonResponse({'message': 'OTP verified successfully!'})
    else:
        return JsonResponse({'error': 'Invalid OTP'}, status=400)

def index(request):
    return render(request,'index.html')