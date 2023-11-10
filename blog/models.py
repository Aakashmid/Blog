from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    sno=models.IntegerField(primary_key=True)
    author=models.CharField( max_length=500)
    title=models.CharField( max_length=500)
    content=models.TextField()
    slug=models.CharField(max_length=200)
    timestamp=models.DateField(auto_now_add=False)

    def __str__(self) -> str:
        return self.title
class blogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timeStamp=models.DateTimeField(default=timezone.now)
    comments=models.TextField()

    def __str__(self) -> str:
        return self.comments + "...  by   "+ self.user.username

