from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import MentorProfile, PersonalProfile, Score, Connections

class MentorProfileAdmin(admin.ModelAdmin):
    search_fields = ['title']

class PersonalProfileAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

admin.site.register(MentorProfile, MentorProfileAdmin)
admin.site.register(PersonalProfile, PersonalProfileAdmin)
admin.site.register(Score)
admin.site.register(Connections)