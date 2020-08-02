from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class PersonalProfile(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    credit = models.PositiveSmallIntegerField(default=0)
    credit_used = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user_id


class MentorProfile(models.Model):
    # user profile
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_mentor_profile')
    # should get user real name (권기남 멘토) not user_id (gnkwon95). How...?
    # or rather just take as '표기될 이름을 적어주세요' and take it instead.
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_mentor_profile')

    #company
    current_company = models.CharField(max_length=20)
    current_job = models.CharField(max_length=20)
    work_period_from = models.DateField()
    work_period_to = models.DateField(null=True, blank=True) #use front to write '현재' if datetime is null

    #spec
    #MentorProfileCertificates=models.ForeignKey(MentorProfileCertificates)
    #MentorProfileExtracurricular
    #MentorProfileWorkExperience
    #MentorProfileAppliedCompanies

    # self introduction
    PR = models.TextField()

    #votes
    voter = models.ManyToManyField(User, related_name='voter_profile')

    #account
    real_name = models.CharField(max_length=20)
    phone_number = models.BigIntegerField()
    bank = models.CharField(max_length=20, default='') #아마 툴로 따로 처리할듯
    account_num = models.BigIntegerField() #이것도 아마 툴로 따로 처리할듯
    account_email = models.CharField(max_length=20, default='') # 디폴트를 로그인때 받은 값으로 전달받아야함... 어떻게?

    #other
    create_date = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

class MentorProfileCertificates(models.Model):
    profile = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileExtracurricular(models.Model):
    profile = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    extracurricular = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileWorkExperience(models.Model):
    profile = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    workexperience = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileAppliedCompanies(models.Model):
    profile = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    appliedcompany = models.CharField(max_length=20)
    appliedcompanystage = models.CharField(max_length=20, default='최종합')

    def __str__(self):
        return str(self.profile.user_id)


class Comment(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE) #개인 정보 가져오기
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_comment')
    date_modified = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_comment')

class Score(models.Model):
    granted_by = models.ForeignKey(User, default=0, on_delete=models.PROTECT)
    #settings.USER_AUTH__MODEL
    granted_to = models.ForeignKey(MentorProfile, default=0, related_name="granted_to", on_delete=models.PROTECT)
    score = models.PositiveSmallIntegerField(default=0) #dropdown, 1 to 5
    created_at = models.DateTimeField('date published')

# Create your models here.

class Connections(models.Model):
    mentor = models.ForeignKey(MentorProfile, on_delete=models.PROTECT, related_name='connection_mentor')
    mentee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='connection_mentee')
    registered_date = models.DateField('date published')
    meeting_date = models.DateField()
