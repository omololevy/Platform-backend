from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(PublicCohort)
admin.site.register(Fundraiser)
admin.site.register(PrivateCohort)
admin.site.register(Post)
admin.site.register(GroupMember)
