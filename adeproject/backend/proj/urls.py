from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from proj import views

router = DefaultRouter()
router.register(r'profiles', views.ProfilesViewSet)
router.register(r'mypage', views.PersonalViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]