from django.db import models

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(max_length=100)
    f_name = models.CharField(max_length=20)
    tel_number = models.CharField(max_length=14)