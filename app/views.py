from django.contrib.auth.models import User
from .models import Profile, PublicCohort, privateCohort
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, UserProfileSerializer, PublicCohortSerializer, PrivateCohortSerializer


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
    permission_classes = [permissions.IsAuthenticated]


class PublicCohortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public cohorts to be created.
    """
    queryset = PublicCohort.objects.all().order_by('-id')
    serializer_class = PublicCohortSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PrivateCohortViewSet(viewsets.ModelViewSet):
    queryset = privateCohort.objects.all()
    serializer_class = PrivateCohortSerializer
