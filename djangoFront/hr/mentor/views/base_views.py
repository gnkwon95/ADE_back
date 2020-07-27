from django.shortcuts import render, get_object_or_404
from ..models import Profile
from django.core.paginator import Paginator
from django.db.models import Q, Count

def index(request):
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어 추가
    so = request.GET.get('so', 'recent') #정렬 기준

    if so == 'recommend':
        profile_list = Profile.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so=='popular':
        profile_list=Profile.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:
        profile_list=Profile.objects.order_by('-create_date')

    if kw:
        profile_list=profile_list.filter(
            Q(title__icontains=kw) |
            Q(author__icontains=kw) |
            Q(school__icontains=kw) |
            Q(workExperience__icontains=kw) |
            Q(PR__icontains=kw) |
            Q(comment__user_id__username__icontains=kw)
        ).distinct()

    paginator = Paginator(profile_list, 10)
    page_obj = paginator.get_page(page)

    context = {'profile_list': page_obj, 'page': page, 'kw': kw, 'so': so}

    return render(request, 'mentor/profile_list.html', context)

# Create your views here.
def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    context = {'profile': profile}
    return render(request, 'mentor/profile_detail.html', context)


"""
@login_required(login_url='common:login')
def repl_create(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.method == "POST":
        form = ReplForm(request.POST)
        if form.is_valid():
            repl = form.save(commit=False)
            repl.create_date = timezone.now()
            repl.profile = profile
            repl.user_id = request.user
            repl.save()
            return redirect('mentor:detail', profile_id=profile.id)
    else:
        form = ReplForm()
    context = {'form': form}
    return render(request, 'mentor/repl_form.html', context)

@login_required(login_url='common:login')
def repl_modify(request, repl_id):
    repl = get_object_or_404(Repl, pk=repl_id)
    if request.user != repl.user_id:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('mentor:detail', profile_id=repl.profile.id)

    if request.method == "POST":
        form = ReplForm(request.POST, instance=repl)
        if form.is_valid():
            repl = form.save(commit=False)
            repl.user_id = request.user
            repl.modify_date = timezone.now()
            repl.save()
            return redirect('mentor:detail', profile_id=repl.profile.id)
    else:
        form = ReplForm(instance=repl)
    context = {'form': form}
    return render(request, 'mentor/repl_form.html', context)

@login_required(login_url='common:login')
def repl_delete(request, repl_id):
    repl = get_object_or_404(Repl, pk=repl_id)
    if request.user!= repl.user_id:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('mentor:detail', profile_id=repl.profile_id)
    repl.delete()
    return redirect('mentor:index', profile_id=repl.profile_id)

"""
