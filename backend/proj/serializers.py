from rest_framework import serializers
from .models import MentorProfile, User, Comment, Score, Connections, MentorProfileAppliedCompanies, MentorProfileCertificates, MentorProfileExtracurricular, MentorProfileWorkExperience



class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_uid', 'email', 'user_id', 'credit', 'credit_used')
        read_only_fields = ('credit', 'credit_used')

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileCertificates
        fields = ('profile', 'certificate')

class ExtracurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileExtracurricular
        fields = ('profile', 'extracurricular')

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileWorkExperience
        fields = ('profile', 'workexperience')

class AppliedCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfileAppliedCompanies
        fields = ('profile', 'appliedcompany', 'appliedcompanystage')

class MentorProfileSerializer(serializers.ModelSerializer):
  #  certificates = CertificateSerializer(many=True, source='certificates_set')
  #  extracurricular = ExtracurricularSerializer(many=True, source='extracurricular_set')
  #  workexperience = WorkExperienceSerializer(many=True, source='workexperience_set')
  #  appliedCompanies = AppliedCompaniesSerializer(many=True, source='appliedcompanies_set')

    class Meta:
        model = MentorProfile
        fields = ('user', 'current_company', 'current_job',
                  'work_period_from', 'work_period_to',
                  'PR', 'voter', 'real_name',
                  'phone_number', 'bank', 'account_num', 'account_email',
                  'create_date', 'date_modified')


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

    class Meta:
        model = Connections
        fields = ('mentor', 'mentee', 'registered_date', 'meeting_date', 'mentor_uid', 'mentee_uid')



#MentorProfileCertificates
    #MentorProfileExtracurricular
    #MentorProfileWorkExperience
    #MentorProfileAppliedCompanies