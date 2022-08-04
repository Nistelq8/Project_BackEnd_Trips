from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Trip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True)
    bio = models.CharField(max_length=300,)
    id = models.AutoField(primary_key=True)
    trips = models.ForeignKey(Trip,on_delete=models.CASCADE, related_name="trip")
    def __str__(self):
        return self.user.username

    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance, bio="",)

    post_save.connect(create_profile, sender=User)