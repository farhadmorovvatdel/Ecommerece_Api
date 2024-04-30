from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   phone_number = models.CharField(max_length=15,unique=True) 
   def __str__(self):
       return self.phone_number
      