from rest_framework import serializers
from .models import MentorProfile, User, Comment, Score, Connections, MentorProfileExtracurricular, MentorProfileCertificates,  MentorProfileWorkExperience, MentorProfileAppliedCompanies, Logger



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
        fields = ['company', 'work_from_year', 'work_from_month', 'work_to_year', 'work_to_month']

class ExtracurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileExtracurricular
        fields = ['extracurricular']

class AppliedCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileAppliedCompanies
        fields = [ 'company']

class MentorProfileSerializer(serializers.ModelSerializer):
    Profile= PersonalSerializer(many=True, read_only=True)

    class Meta:
        model = MentorProfile
        fields = ['user', 'nickname', 'education_univ', 'education_major',
                  'education_level', 'education_status', 'current_company',
                  'logo', 'current_job', 'applied_job',
                  'work_start_year', 'work_start_month',
                  'PR', 'intro', 'voter', 'card_user_name',
                  'bank', 'account_num', 'account_email',
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
    Certificate = CertificateSerializer(many=True)
    AppliedCompanies = AppliedCompaniesSerializer(many=True)
    WorkExperience = WorkExperienceSerializer(many=True)
    Extracurricular = ExtracurricularSerializer(many=True)


    class Meta:
        model = MentorProfile
        depth=1
        fields = ['user', 'nickname', 'education_univ', 'education_major',
                  'education_level', 'education_status', 'current_company',
                  'logo', 'current_job', 'applied_job',
                   'work_start_year', 'work_start_month',
                  'PR', 'intro', 'voter', 'card_user_name',
                  'bank', 'account_num', 'account_email',
                  'create_date', 'date_modified', 'Certificate', 'AppliedCompanies', 'WorkExperience', 'Extracurricular']


class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logger
        fields = ['user', 'user_id', 'user_uid', 'time', 'page', 'detail']


#MentorProfileCertificates
    #MentorProfileExtracurricular
    #MentorProfileWorkExperience
    #MentorProfileAppliedCompanies