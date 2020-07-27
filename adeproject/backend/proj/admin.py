from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import Profile, PersonalProfile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['title']

class PersonalAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

admin.site.register(Profile)
admin.site.register(PersonalProfile)