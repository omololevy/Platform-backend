from django.contrib.auth.models import User
from django.http import JsonResponse
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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from app import serializers

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class GetProfile(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    lookup_field = 'id'
    queryset = Profile.objects.first()

    def get(request):
        serializer = UserProfileSerializer()
        if serializer.is_valid():
            serializer.get_fields()
            return Response('hello')
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ProfileUpdateView(generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'email'
    queryset = Profile.objects.all()
  
    def put(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    # y = Profile.
    # permission_classes = [permissions.IsAuthenticated]

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def profile_detail(request, pk):
    #     # find tutorial by pk (id)
    #     try: 
    #         profile = Profile.objects.get(pk=pk) 
    #     except Profile.DoesNotExist: 
    #         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

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
    
