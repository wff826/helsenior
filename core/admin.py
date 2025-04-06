from django.contrib import admin
from .models import Elder, Caregiver, HealthData, Alert

admin.site.register(Elder)
admin.site.register(Caregiver)
admin.site.register(HealthData)
admin.site.register(Alert)
