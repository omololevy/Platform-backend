from django.contrib.auth.models import User
from .models import PrivateCohort, Profile,PublicCohort,Fundraiser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication 
from .serializers import UserSerializer,UserProfileSerializer,PublicCohortSerializer,UserCreateSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
# authentication
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer,UserProfileSerializer,PublicCohortSerializer,FundraiserSerializer,PrivateCohortSerializer,SmsSerializer
from app.permissions import IsAdminOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

class UserList(APIView): # list all users
    """
    List all users.
    """
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.filter(profile__isDoctor=False).values("id", "first_name", "second_name", "email").all()
        user_id = request.query_params.get('user_id')
        if user_id:
            user = User.objects.get(id=user_id)
            profile = user.profile
            serializer = UserSerializer(user)
            data = serializer.data
            data["user_id"] = user.id
            data["tel_number"] = profile.tel_number
            data["email"] = profile.email
            users = data
        return Response(users)


class UserCreate(APIView): # create user
    """
    Create a user.
    """

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginUser(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                profile = user.profile
                serializer = UserSerializer(user)
                data = serializer.data
                data["user_id"] = user.id
                data["email"] = profile.email
                data["tel_number"] = profile.tel_number
                return Response(data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# ProfileList
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# ProfileDetail
class ProfileDetail(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    # def get_object(self, pk):
    #     try:
    #         return Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializers = ProfileSerializer(profile, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class PublicCohortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public cohorts to be created.
    """
    queryset = PublicCohort.objects.all().order_by('-id')
    serializer_class = PublicCohortSerializer
    permission_classes = [permissions.IsAuthenticated]

    # logout user ====================================
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
    
class SendSmsMessage(APIView): # create user

    # show either error message for sending sms or success message
    def on_finish(error, response):
        if error is not None:
            raise error
        print(response)

    # def post(self, request, format=None):  # create appointment
    #     serializer = SmsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         # get the phone number from the appointment and send sms
    #         phone_number = serializer.data['phone']
    #         print(phone_number)
    #         message = "Welcome to the Moringa Alumni Platform"
    #         sms.send(message, [phone_number])
    #         # get the admin phone number and send sms ============================
    #         # admin_phone_number = User.objects.get(username='admin').phone
    #         # sms.send("New appointment created ", [admin_phone_number], callback=self.on_finish)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
