from django.contrib import admin


from .models import privateCohort
from .models import PublicCohort
from .models import Profile
# Register your models here.

admin.site.register(privateCohort)
admin.site.register(PublicCohort)
admin.site.register(Profile)
