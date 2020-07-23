from django import forms
from .models import Profile, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title', 'author','school', 'workExperience', 'PR']
        labels = {
            'title': '제목',
            'author': '멘토 성명',
            'school': '출신 학교',
            'workExperience': '합격 전 이력',
            'PR': '자기소개',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '후기',
        }

"""
class ReplForm(forms.ModelForm):
    class Meta:
        model = Repl
        fields = ['content']
        labels = {
            'content': '대댓내용',
        }

"""