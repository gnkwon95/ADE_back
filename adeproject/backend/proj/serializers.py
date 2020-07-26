from rest_framework import serializers
from .models import Profile, Mypage, PersonalProfile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('title', 'author', 'user_id', 'create_date',
              'date_modified', 'school', 'workExperience', 'PR', 'voter')

class MypageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mypage
        fields = ('user_id', 'user_pw')

class PersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = ('user_id', 'email', 'user_name', 'user_pw', 'credit', 'credit_used')
