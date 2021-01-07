from django.contrib import admin
from .models import CareersOpportunity, Teams, Applicant

# Register your models here.
admin.register(CareersOpportunity, Teams, Applicant)(admin.ModelAdmin)
