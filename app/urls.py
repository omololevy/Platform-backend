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
    path('fundraiser/',views.FundraiserSerializer),
    path('privatecohort/', views. PrivateCohortSerializer),
]
