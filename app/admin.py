from django.contrib import admin

from .models import Profile,PublicCohort,Fundraiser

#Registering models
admin.site.register(PublicCohort)
admin.site.register(Profile)
admin.site.register(Fundraiser)
