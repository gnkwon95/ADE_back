from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    title = models.CharField(max_length = 100)
    user_name = models.CharField(User, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date published')
    school = models.CharField(max_length = 100)
    date_modified = models.DateTimeField(null=True, blank=True)
    workExperience = models.CharField(max_length = 200)
    PR = models.TextField()
    voter = models.ManyToManyField(User, related_name='voter_profile')

    def __str__(self):
        return self.title

class PersonalProfile(models.Model):
#    REQUIRED_FIELDS = ('user_id', 'user_pw')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_pw = models.CharField(User, on_delete=models.CASCADE)
    credit = models.PositiveSmallIntegerField(default=0)
    credit_used = models.PositiveSmallIntegerField(default=0)



class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_profile')
    date_modified = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_comment')
# Create your models here.