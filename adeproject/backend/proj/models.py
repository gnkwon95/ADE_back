from django.db import models
from django.contrib.auth.models import User

class PersonalProfile(models.Model):
#    REQUIRED_FIELDS = ('user_id', 'user_pw')
    user_id = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    credit = models.PositiveSmallIntegerField(default=0)
    credit_used = models.PositiveSmallIntegerField(default=0)


class Profile(models.Model):
    title = models.CharField(max_length = 100)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_profile')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_profile')
    create_date = models.DateTimeField('date published')
    school = models.CharField(max_length = 100)
    date_modified = models.DateTimeField(null=True, blank=True)
    workExperience = models.CharField(max_length = 200)
    PR = models.TextField()
    voter = models.ManyToManyField(User, related_name='voter_profile')

    def __str__(self):
        return self.title

# Create your models here.