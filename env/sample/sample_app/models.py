from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=50)
    year = models.BigIntegerField()

class Navals(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name 