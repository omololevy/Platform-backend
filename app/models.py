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
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{} - {}'.format(self.first_name, self.bio)

    @classmethod
    def get_profile(cls,id):
        user_profile = Profile.objects.filter(user__pk = id)
        return user_profile


class PublicCohort(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    members =   models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='public_members')

    def __str__(self):
        return '{} - {}'.format(self.name, self.description)


class PrivateCohort(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    members =   models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='private_members')


    def __str__(self):
        return '{} - {}'.format(self.name, self.created_by)


class Fundraiser(models.Model):
    fund_name = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return '{}-{}'.format(self.fund_name, self.content)


class Post(models.Model):
    title = models.CharField(max_length=150)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(PublicCohort,on_delete=models.CASCADE,null=True,blank=True)
    group = models.ForeignKey(PrivateCohort,on_delete=models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class GroupMember(models.Model):
    members = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    group = models.ForeignKey(PublicCohort,on_delete=models.CASCADE,null=True,blank=True)
    group2 = models.ForeignKey(PrivateCohort,on_delete=models.CASCADE,null=True,blank=True)
     



