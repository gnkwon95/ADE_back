from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Profile, ProfileAdmin)

# Register your models here.
