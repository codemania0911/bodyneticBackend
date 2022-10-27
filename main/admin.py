from django.contrib import admin

# Register your models here.
from .models import UserData, Profile

admin.site.register(UserData)
admin.site.register(Profile)