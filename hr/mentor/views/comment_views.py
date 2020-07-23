from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Profile, Comment
from django.utils import timezone
from ..forms import ProfileForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='common:login')
def comment_create(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.profile = profile
            comment.user_id = request.user
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('mentor:detail', profile_id=profile.id), comment.id))
    else:
        form = ProfileForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'mentor/profile_detail.html', context)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user_id:
        messages.error(request, '수정권한이 없습니다')
        return redirect('{}#comment_{}'.format(
            resolve_url('mentor:detail', profile_id=comment.profile.id), comment.id))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('mentor:detail', profile_id=comment.profile.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mentor/comment_form.html', context)

## need to create comment_delete
