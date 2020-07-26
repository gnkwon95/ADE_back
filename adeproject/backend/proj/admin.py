from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Profile, ProfileAdmin)