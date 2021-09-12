from django.contrib import admin
from .models import UserProfile, CompanyProfile


admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
