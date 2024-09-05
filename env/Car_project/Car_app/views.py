from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    datas = Cars.objects.all()
    return render(request, 'main.html', {'datas': datas})


def fruits(request):
    fruit = Fruits.objects.all()
    return render(request, 'fruits.html', {'f_datas': fruit})

def videos(request):
    video = Videos.objects.all()
    return render(request, 'movies.html', {'videos': video})