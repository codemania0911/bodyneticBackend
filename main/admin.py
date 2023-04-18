from django.contrib import admin

# Register your models here.
from .models import UserData, Profile, User

admin.site.register(UserData)
admin.site.register(Profile)
admin.site.register(User)