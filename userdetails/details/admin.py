from django.contrib import admin

# Register your models here.
# details/admin.py
from django.contrib import admin
from .models import UserInformation

admin.site.register(UserInformation)
