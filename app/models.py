from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profile_pic = CloudinaryField(null=True)
    bio = models.TextField(max_length=100)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20, null=True)
    tel_number = models.CharField(max_length=14)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.first_name


class PublicCohort(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    # created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return '{} - {}'.format(self.name, self.description)

class PrivateCohort(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField( null=True)
    description = models.TextField(null=True)
    message = models.TextField(verbose_name="Message",null=True)
    created_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.created_by)

class Fundraiser(models.Model):
    fund_name = models.CharField(max_length=30, unique=True)  
    created_by = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    start_date = models.DateTimeField()  
    end_date = models.DateTimeField()
    
    def __str__(self):
        return '{}-{}'.format(self.fund_name, self.content)


    
