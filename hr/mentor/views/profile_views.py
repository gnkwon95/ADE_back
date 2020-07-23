from django.shortcuts import render, get_object_or_404, redirect
from ..models import Profile, Comment
from django.utils import timezone
from ..forms import ProfileForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.create_date = timezone.now()
            profile.user_id = request.user
            profile.save()
            return redirect('mentor:index')
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'mentor/profile_form.html', context)

@login_required(login_url = 'common:login')
def profile_modify(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.user != profile.user_id:
        messages.error(request, '수정권한이 없습니다')
        return redirect('mentor:detail', profile_id=profile.id)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user_id = request.user
            profile.modify_date=timezone.now()
            profile.save()
            return redirect('mentor:detail', profile_id=profile.id)
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'mentor/profile_form.html', context)

@login_required(login_url='common:login')
def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.user!= profile.user_id:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('mentor:detail', profile_id=profile.id)
    profile.delete()
    return redirect('mentor:index')