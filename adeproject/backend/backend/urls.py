from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers  # add this
from proj import views  # add this

"""
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
"""



router = routers.DefaultRouter()  # add this
router.register(r'profiles', views.ProfileListView, 'profile')  # add this
#router.register(r'profiles/([0-9]+)$', views.ProfileView, 'profilelist')
router.register(r'mypage', views.MypageView, 'mypage')
router.register(r'^profiles/(?P<pk>[0-9]+)/$', views.PersonalProfileView, 'personalprofile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # add this
 #   path('api/mypage', include(router.urls), name='mypage'),
  #  path('api/mypage', include(mypage.urls), name=',mypage'),
]