from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)
    def __str__(self):
        return self.fname

class note(models.Model):
    user = models.ForeignKey(register, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.title

