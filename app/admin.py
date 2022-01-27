from django.contrib import admin
from .models import *


from .models import privateCohort
from .models import PublicCohort
# Register your models here.
admin.site.register(Profile)
admin.site.register(PublicCohort)
admin.site.register(Fundraiser)
admin.site.register(PrivateCohort)
