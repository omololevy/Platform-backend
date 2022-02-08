from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile,PublicCohort,Fundraiser,PrivateCohort, Sms


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        # print(validated_data)
        # print('Hello')
        return user

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'first_name', 'second_name', 'bio', 'tel_number', 'email', 'user')

    def create_profile(self, data):
        profile = Profile.objects.create_profile(**data)
        return profile


class PublicCohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicCohort
        fields = ('name', 'description')
        read_only_fields = ('owner', 'date_created', 'date_updated', 'created_by')

    def create_public_cohort(self, cohort_data):
        public_cohort = PublicCohort.objects.create_public_cohort(
            **cohort_data)
        return public_cohort

class PrivateCohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateCohort
        fields = ('timestamp', 'date_updated', 'name',
                  'description', 'message', 'created_by')

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraiser
        fields = ('fund_name','content','start_date', 'end_date','created_by')
        
    def create_fundraiser(self,fundraiser_data):
        fundraiser = Fundraiser.objects.create_profile(**fundraiser_data)
        return fundraiser

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'first_name', 'second_name', 'bio', 'tel_number', 'email', 'user')

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = ['first_name', 'email', 'phone']