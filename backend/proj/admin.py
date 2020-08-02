from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import MentorProfile, PersonalProfile, Score, Comment, Connections, MentorProfileWorkExperience, MentorProfileExtracurricular, MentorProfileCertificates, MentorProfileAppliedCompanies

class MentorProfileAdmin(admin.ModelAdmin):
    search_fields = ['title']

class PersonalProfileAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

admin.site.register(MentorProfile, MentorProfileAdmin)
admin.site.register(PersonalProfile, PersonalProfileAdmin)
admin.site.register(Score)
admin.site.register(Connections)

admin.site.register(MentorProfileWorkExperience)
admin.site.register(MentorProfileExtracurricular)
admin.site.register(MentorProfileCertificates)
admin.site.register(MentorProfileAppliedCompanies)
admin.site.register(Comment)