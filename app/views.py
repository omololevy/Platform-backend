from django.contrib.auth.models import User
from django.shortcuts import render
from .models import PrivateCohort, Profile,PublicCohort,Fundraiser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication 
from .serializers import UserSerializer,UserProfileSerializer,PublicCohortSerializer,FundraiserSerializer,PrivateCohortSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
# authentication
from django.contrib.auth import authenticate, login, logout

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PublicCohortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public cohorts to be created.
    """
    queryset = PublicCohort.objects.all().order_by('-id')
    serializer_class = PublicCohortSerializer
    # permission_classes = [permissions.IsAuthenticated]

class logoutUser(APIView): # logout user
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class FundraiserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public cohorts to be created.
    """
    queryset = Fundraiser.objects.all().order_by('-id')
    serializer_class = FundraiserSerializer

class PrivateCohortViewSet(viewsets.ModelViewSet):
    queryset = PrivateCohort.objects.all()
    serializer_class = PrivateCohortSerializer
    
