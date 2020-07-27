from rest_framework import serializers
from .models import Profile, PersonalProfile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('title', 'user_name', 'user_id', 'create_date',
              'date_modified', 'school', 'workExperience', 'PR', 'voter')

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = ('user_id', 'email', 'user_name', 'user_pw', 'credit', 'credit_used')
