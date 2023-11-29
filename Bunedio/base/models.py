from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

# Topic -> PostContent -> Comment

class Topic(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    body = models.TextField(null=False,blank=False,default="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # deleted id due to unneeded usage
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.ForeignKey(Post,on_delete=models.CASCADE,null=False)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
