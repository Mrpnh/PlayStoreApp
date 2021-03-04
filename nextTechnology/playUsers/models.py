from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    points=models.IntegerField(default=0)
    tasks=models.IntegerField(default=0)
    downloaded=models.JSONField(default=list)
    screenshot=models.ImageField(default='default.jpg',upload_to='screenshots')