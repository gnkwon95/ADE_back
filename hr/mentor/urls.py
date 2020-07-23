from django.urls import path
#from . import views

from .views import base_views, profile_views, comment_views, vote_views

app_name = 'mentor'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name = 'index'),
    path('<int:profile_id>/', base_views.detail, name='detail'),

    #profile_views.py
    path('profile/create/', profile_views.profile_create, name='profile_create'),
    path('profile/modify/<int:profile_id>/', profile_views.profile_modify, name='profile_modify'),
    path('profile/delete/<int:profile_id>/', profile_views.profile_delete, name='profile_delete'),

    #comment_views.py
    path('comment/create/<int:profile_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),

    #vote_views.py
    path('vote/profile/<int:profile_id>/', vote_views.vote_profile, name='vote_profile'),
    path('vote/comment/<int:comment_id>/', vote_views.vote_comment, name='vote_comment'),

    #repl_views.py
    #path('repl/create/profile/<int:profile_id>/', views.repl_create, name='repl_create'),
    #path('repl/modify/profile/<int:repl_id>/', views.repl_modify, name='repl_modify'),
    #path('repl/delete/profile/<int:crepl_id>/', views.repl_delete, name='repl_delete'),
]