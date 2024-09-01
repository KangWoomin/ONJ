from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','birth','nickname']
    list_display_links = ['email','nickname']

admin.site.register(User, UserAdmin)