# from django.db import models

# Create your models here.
# accounts/models.py
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # It's important to hash passwords

    def __str__(self):
        return self.username
    

class Contact(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

class contentImages(models.Model):
    profile_image = models.ImageField(upload_to='media/')


