from django.contrib import admin


# Register your models here.


# New Code since deployment

from django.contrib import admin
from .models import UserProfile, CompanyProfile

admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
