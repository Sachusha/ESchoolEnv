from django.contrib import admin
from .models import *
# Register your models here.


class StudentProfileAdmin(admin.ModelAdmin):
    fields = ['profile_name', 'profile_address', 'profile_contactno', 'profile_email']


admin.site.register(SchoolProfile, StudentProfileAdmin)