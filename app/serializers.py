from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic','first_name','second_name','bio','tel_number','email','user')
    
    def create_profile(self,data):
        profile = Profile.objects.create_profile(**data)
        return profile