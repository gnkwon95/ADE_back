from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date published')
    school = models.CharField(max_length = 100)
    date_modified = models.DateTimeField(null=True, blank=True)
    workExperience = models.CharField(max_length = 200)
    PR = models.TextField()
    voter = models.ManyToManyField(User, related_name='voter_profile')

    def __str__(self):
        return self.title

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_profile')
    date_modified = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_comment')
# Create your models here.

"""
class Repl(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
"""