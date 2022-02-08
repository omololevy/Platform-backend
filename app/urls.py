from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.UserProfileViewSet)
router.register(r'public-cohort',views.PublicCohortViewSet)
router.register(r'fundraiser',views.FundraiserViewSet)
router.register(r'private-cohort', views. PrivateCohortViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', ObtainAuthToken.as_view()),
    path('profile/',views.UserProfileSerializer),
    path('public-cohort/',views.PublicCohortSerializer),
    path('api/auth/logout/', views.logoutUser.as_view()),


    path('fundraiser/',views.FundraiserSerializer),
    path('privatecohort/', views. PrivateCohortSerializer),

    path('profiles/', views.ProfileList.as_view()), # list of profiles
    path('profiles/<pk>[0-9]+/', views.ProfileDetail.as_view()), # single profile
    path('users/', views.UserList.as_view()), # list of users
    path('users/create/', views.UserCreate.as_view()), # create user
    path('auth/login/', views.loginUser.as_view()), # login user
    path('auth/logout/', views.logoutUser.as_view()), # logout user
    # path('/vaccine/', views.VaccineList.as_view(), name="vaccines"),
    # path('medicalhistory/', views.MedicalHistoryList.as_view(), name="medicalHistory"),
    # path('growth/', views.GrowthList.as_view(), name="growth"),
    # path('vaccines/<int:pk>/', views.VaccineDetail.as_view(), name="vaccines_detail"),
    path('send-message',views.SendSmsMessage.as_view(),name="sms-message")
]
