from pyexpat import model
from django.db import models

# Create your models here.

class Operations(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_name= models.CharField(max_length=100)