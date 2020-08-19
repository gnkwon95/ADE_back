from rest_framework import serializers
from .models import MentorProfile, User, Comment, Score, Connections, MentorProfileAppliedCompanies, MentorProfileCertificates,  MentorProfileWorkExperience



class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_uid', 'email', 'user_id', 'credit', 'credit_used', 'is_mentor')
        read_only_fields = ('credit', 'credit_used')

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileCertificates
        fields = ['certificate']

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileWorkExperience
        fields = [ 'workexperience']

class AppliedCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileAppliedCompanies
        fields = ['appliedcompany', 'appliedcompanystage']

class MentorProfileSerializer(serializers.ModelSerializer):
    Profile= PersonalSerializer(many=True, read_only=True)


    class Meta:
        model = MentorProfile
        fields = ['user', 'nickname', 'current_company', 'logo', 'current_job',
                  'work_period_from', 'work_period_to',
                  'PR', 'voter', 'real_name',
                  'phone_number', 'bank', 'account_num', 'account_email',
                  'create_date', 'date_modified', 'Profile']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('profile', 'user_id', 'date_modified', 'content', 'create_date', 'voter')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('granted_by', 'granted_to', 'score', 'created_at')

class ConnectionsSerializer(serializers.ModelSerializer):
    mentor_uid = serializers.ReadOnlyField(source='mentor.user.user_uid')
    mentee_uid = serializers.ReadOnlyField(source='mentee.user_uid')
    mentor_id = serializers.ReadOnlyField(source='mentor.user.user_id')
    mentee_id = serializers.ReadOnlyField(source='mentee.user_id')

    class Meta:
        model = Connections
        fields = ('mentor', 'mentee', 'registered_date', 'meeting_date', 'mentor_uid', 'mentee_uid', 'mentor_id', 'mentee_id')

class MentorSerializer(serializers.ModelSerializer):
    Certificate = CertificateSerializer(many=True, read_only=True)
    AppliedCompanies = AppliedCompaniesSerializer(many=True, read_only=True)
    WorkExperience = WorkExperienceSerializer(many=True, read_only=True)


    class Meta:
        model = MentorProfile
        depth=1
        fields = ['user', 'nickname', 'current_company', 'current_job',
                  'work_period_from', 'education',
                  'PR', 'voter', 'real_name',
                  'phone_number', 'bank', 'account_num', 'account_email',
                  'create_date', 'date_modified', 'Certificate', 'AppliedCompanies', 'WorkExperience']



#MentorProfileCertificates
    #MentorProfileExtracurricular
    #MentorProfileWorkExperience
    #MentorProfileAppliedCompanies