from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=50)
    year = models.BigIntegerField()


class Fruits(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    qty = models.IntegerField()

class Videos(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/') 


    