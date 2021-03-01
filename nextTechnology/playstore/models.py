from django.db import models

# Create your models here.
class AppAdmin(models.Model):
    name=models.CharField(max_length=100)
    appID=models.CharField(max_length=100)
    iconLink=models.CharField(max_length=150)
    category=models.CharField(max_length=100,default="Other")
    points=models.IntegerField()
