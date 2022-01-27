from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profile_pic = CloudinaryField('profile_photos/', default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.TextField(max_length=100)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20, null=True)
    tel_number = models.CharField(max_length=14)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name


class PublicCohort(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return '{}-{}'.format(self.name, self.description)


class privateCohort(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(verbose_name="Name", max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    message = models.TextField(verbose_name="Message", blank=True, null=True)
    created_by = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
