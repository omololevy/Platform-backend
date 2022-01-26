from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profile_pic = CloudinaryField(null=True)
    bio = models.TextField(max_length=100)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20,null=True)
    tel_number = models.CharField(max_length=14)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.first_name


class PublicCohort(models.Model):
    name = models.CharField(max_length=128 ,unique=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return '{}-{}'.format(self.name, self.description)
    