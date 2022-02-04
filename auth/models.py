from pyexpat import model
from django.db import models

# Create your models here.

# Create Form

class form(models.Model):
   
    user_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
