from django.contrib import admin
from django.urls import path, include
from mentor.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentor/', include('mentor.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
