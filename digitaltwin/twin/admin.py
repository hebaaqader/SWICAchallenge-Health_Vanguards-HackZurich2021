from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(HealthFacility)
admin.site.register(Practitioner)
admin.site.register(Insurance)
admin.site.register(Case)