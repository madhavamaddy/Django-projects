# accounts/decorators.py
from django.shortcuts import redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrap
