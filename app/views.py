from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http import JsonResponse, Http404
from .serializers import   UserProfileSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from .models import Profile
from rest_framework import viewsets, status, generics, permissions, serializers
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.settings import perform_import
from rest_framework.response import Response
from rest_framework.views import APIView
from decouple import config, Csv
import africastalking


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]