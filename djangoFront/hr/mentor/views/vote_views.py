from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Profile, Comment

@login_required(login_url='common:login')
def vote_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.user == profile.user_id:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다")
    else:
        profile.voter.add(request.user)
    return redirect('mentor:detail', profile_id=profile.id)

@login_required(login_url='common:login')
def vote_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user_id:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        comment.voter.add(request.user)
    return redirect('mentor:detail', profile_id=comment.profile.id)