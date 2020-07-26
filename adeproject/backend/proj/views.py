from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import ProfileSerializer, MypageSerializer, PersonalProfileSerializer      # add this
from .models import Profile, Mypage, PersonalProfile
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    """
    콘텐츠를 JSON으로 변환한 후 HttpResponse 형태로 반환합니다.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class ProfileListView(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()

class MypageView(viewsets.ModelViewSet):
    serializer_class=MypageSerializer
    queryset=Mypage.objects.all()

def PersonalProfileView(request, pk):
    try:
        personalprofile = Profile.object.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PersonalProfileSerializer(personalprofile)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonalProfileSerializer(personalprofile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, stuats=400)

    elif request.method == 'DELETE':
        personalprofile.delete()
        return HttpResponse(status=204)

#결론: serializer 쓰지 말자......


    """

    def snippet_detail(request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)

    */"""