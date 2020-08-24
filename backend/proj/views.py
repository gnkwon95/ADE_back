from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import MentorProfileSerializer, PersonalSerializer, CommentSerializer, ScoreSerializer, ConnectionsSerializer, WorkExperienceSerializer, CertificateSerializer, ExtracurricularSerializer, MentorSerializer, LoggerSerializer
from .models import MentorProfile, User, Comment, Score, Connections, MentorProfileCertificates,  MentorProfileWorkExperience, MentorProfileExtracurricular, Logger
from rest_framework_tracking.mixins import LoggingMixin

class MentorProfilesViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()


class PersonalViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = PersonalSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user_uid = user)
        return queryset

class CommentViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        profile = self.request.query_params.get('profile', None)
        if profile is not None:
            queryset = queryset.filter(profile = profile)
        return queryset

class ScoreViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = ScoreSerializer

    def get_queryset(self):
        queryset = Score.objects.all()
        granted_to = self.request.query_params.get('granted_to', None)
        if granted_to is not None:
            queryset = queryset.filter(granted_to = granted_to)
        return queryset


class ConnectionsViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class=ConnectionsSerializer
  #  queryset = Connections.objects.all()

    def get_queryset(self):
        queryset = Connections.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        mentee = self.request.query_params.get('mentee', None)
        user = self.request.query_params.get('user', None)
        if mentor is not None:
            queryset = queryset.filter(mentor = mentor)
        if mentee is not None:
            queryset = queryset.filter(mentee = mentee)
        if user is not None:
            queryset1 = queryset.filter(mentor__user__user_uid = str(user)) #or mentee. filter on two fields.
            queryset2 = queryset.filter(mentee__user_uid = str(user))
            return queryset1 | queryset2
        return queryset



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


class WorkExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkExperienceSerializer

    def get_queryset(self):
        queryset = MentorProfileWorkExperience.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile=mentor)
        return queryset

class ExtracurricularViewSet(viewsets.ModelViewSet):
    serializer_class = ExtracurricularSerializer
    queryset = MentorProfileExtracurricular.objects.all()

    def get_queryset(self):
        queryset = MentorProfileExtracurricular.objects.all()
        mentor = self.request.query_params.get('mentor', None)
        if mentor is not None:
            queryset = queryset.filter(profile=mentor)
        return queryset

class ProfileFullViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSerializer

    def get_queryset(self):
        queryset = MentorProfile.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user__user_uid=user)
        return queryset

class LoggerViewSet(viewsets.ModelViewSet):
    serializer_class = LoggerSerializer
    queryset = Logger.objects.all()