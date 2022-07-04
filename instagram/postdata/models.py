from distutils.command.upload import upload
from email.mime import audio
from operator import truediv
from django.db import models
from django.conf import settings



class Post(models.Model):
    caption=models.CharField(max_length=2200)
    img=models.ImageField(upload_to='images/')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    like=models.IntegerField(default=0,null=True,blank=True)

class Comment(models.Model):

    text=models.CharField(max_length=255)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True,related_name='posts')
    