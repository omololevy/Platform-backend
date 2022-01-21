from django.contrib.auth.models import User
from .models import Profile
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,UserProfileSerializer


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