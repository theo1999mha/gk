from django.db import models
from users.models import User
from django.utils import timezone

class Post(models.Model):
    STATUS_CHO = (
        ('DRAFT',0),
        ('PUBLISH',1)   
    )
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0,choices=STATUS_CHO)
    title = models.CharField(max_length=60)
    description = models.TextField(null=True ,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True ,null=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Like(models.Model):
    post_id = models.ForeignKey(Post ,on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE ,null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    body = models.TextField(null=True , blank=True)
    post_id = models.ForeignKey(Post ,on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE,null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    