from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import ProfileSerializer, PersonalSerializer      # add this
from .models import Profile, PersonalProfile
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics

class ProfilesViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



class PersonalViewSet(viewsets.ModelViewSet):
    queryset = PersonalProfile.objects.all()
    serializer_class = PersonalSerializer