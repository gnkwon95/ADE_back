from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from proj import views

router = DefaultRouter()
router.register(r'profiles', views.MentorProfilesViewSet) #for front page, get all list
    #for detail page, access profiles/<mentor_number>
router.register(r'mypage', views.PersonalViewSet) #will query into mypage/<my_number> (although shown as /mypage/)
router.register(r'comments', views.CommentViewSet) # will not display on url
router.register(r'scores', views.ScoreViewSet) #will not display on url
router.register(r'connections', views.ConnectionsViewSet, basename='connections') #get all connections, and query queries related to myself

#used to get mentor profiles, get input
# for example, axios.get('certificates/?mentor=1') would get list of certificates for mentor 1
router.register(r'certificates', views.CertificateViewSet, basename='profile-certificates') #used as query on mentor profile
router.register(r'extracurricular', views.ExtracurricularViewSet, basename='profile-extracurricular')
router.register(r'workexperience', views.WorkExperienceViewSet, basename='profile-workexperience')
router.register(r'appliedcompanies', views.AppliedCompaniesViewSet, basename='profile-appliedcompanies')


urlpatterns = [
    url(r'^', include(router.urls))
]