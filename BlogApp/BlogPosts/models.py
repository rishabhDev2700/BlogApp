from django.db import models

# Create your models here.
from Authentication.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.TextField(max_length=100)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    objects = models.manager


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=4000)
    cover = models.ImageField(upload_to='cover/', blank=True)
    pub_date = models.DateTimeField(auto_created=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    objects = models.manager
