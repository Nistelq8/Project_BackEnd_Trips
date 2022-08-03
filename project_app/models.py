from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    id = models.AutoField(primary_key=True)
    
    