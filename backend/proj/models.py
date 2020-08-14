from django.db import models
from django.utils import timezone

class User(models.Model):
    user_uid = models.CharField(max_length=50) #input as user_uid from django
    email = models.EmailField(max_length=50) #input as email from django
    user_id = models.CharField(max_length=20) #input as username from django
    credit = models.PositiveSmallIntegerField(default=0)
    credit_used = models.PositiveSmallIntegerField(default=0)
    is_mentor = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id

class MentorProfile(models.Model):
    # mentor profile
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_profile_user')

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
    voter = models.ManyToManyField(User, related_name='voter_profile', blank=True)

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
        return str(self.user.user_id)

class MentorProfileCertificates(models.Model):
    profile = models.ForeignKey(MentorProfile, related_name='Certificates', on_delete=models.CASCADE)
    certificate = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileExtracurricular(models.Model):
    profile = models.ForeignKey(MentorProfile, related_name='Extracurricular', on_delete=models.CASCADE)
    extracurricular = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileWorkExperience(models.Model):
    profile = models.ForeignKey(MentorProfile, related_name='WorkExperience', on_delete=models.CASCADE)
    workexperience = models.CharField(max_length=20)

    def __str__(self):
        return str(self.profile.user_id)

class MentorProfileAppliedCompanies(models.Model):
    profile = models.ForeignKey(MentorProfile, related_name='AppliedCompanies', on_delete=models.CASCADE)
    appliedcompany = models.CharField(max_length=20)
    appliedcompanystage = models.CharField(max_length=20, default='최종합')

    def __str__(self):
        return str(self.profile.user_id)


class Comment(models.Model):
    profile = models.ForeignKey(MentorProfile, on_delete=models.CASCADE) #개인 정보 가져오기
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_comment')
    date_modified = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    voter = models.ManyToManyField(User, blank=True, related_name='voter_comment')

class Score(models.Model):
    granted_by = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    granted_to = models.ForeignKey(MentorProfile, default=0, related_name="granted_to", on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField('date published', default=timezone.now)

# Create your models here.

class Connections(models.Model):
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE, related_name='connection_mentor')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_mentee')
    registered_date = models.DateTimeField( default=timezone.now)
    meeting_date = models.DateField()

    def __str__(self):
        return str(self.mentor.user.user_id + "+" + self.mentee.user_id)
