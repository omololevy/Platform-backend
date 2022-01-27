from django.contrib import admin


from .models import privateCohort
from .models import PublicCohort
# Register your models here.

admin.site.register(privateCohort)
admin.site.register(PublicCohort)
