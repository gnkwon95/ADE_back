from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import MentorProfileSerializer, PersonalSerializer, CommentSerializer, ScoreSerializer, ConnectionsSerializer, CertificateSerializer, ExtracurricularSerializer, AppliedCompaniesSerializer
from .models import MentorProfile, PersonalProfile, Comment, Score, Connections, MentorProfileCertificates, MentorProfileExtracurricular, MentorProfileWorkExperience, MentorProfileAppliedCompanies
from rest_framework_tracking.mixins import LoggingMixin

class MentorProfilesViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()

class PersonalViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = PersonalProfile.objects.all()

class CommentViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class ScoreViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()

class ConnectionsViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class=ConnectionsSerializer
    queryset = Connections.objects.all()



# Mentor Profile related
class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
#

    def get_queryset(self):
        queryset = MentorProfileCertificates.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile = mentor)
        return queryset
"""
    def get_queryset(self):
        user = self.request.user
        return MentorProfileCertificates.objects.filter(profile=user)
"""

class ExtracurricularViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
  #  queryset = MentorProfileExtracurricular.objects.all()

    def get_queryset(self):
        queryset = MentorProfileExtracurricular.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile=mentor)
        return queryset

class WorkExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        queryset = MentorProfileWorkExperience.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile=mentor)
        return queryset

class AppliedCompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = MentorProfileAppliedCompanies.objects.all()

    def get_queryset(self):
        queryset = MentorProfileAppliedCompanies.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile=mentor)
        return queryset
