from django.contrib import admin

# Register your models here.
from .models import Allgroups,Services, patient
admin.site.register(Allgroups)
admin.site.register(Services)
admin.site.register(patient)