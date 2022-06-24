from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator




class UserManager(BaseUserManager):
    
    def creat_costomer_user(self,username,password,**extra_fildes):
        if not username:
            raise ValueError('please inter username')
        user=self.model(
            username=username,**extra_fildes
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,password):
        if not username:
            raise ValueError('Please Inter username')
        superuser=self.model(
            username=username
        )
        superuser.set_password(password)
        superuser.is_staff=True
        superuser.is_superuser=True
        superuser.save()
        return superuser


class User(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(max_length=255,unique=True)
    phonenumber=models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^9[0-9]{9}',message='Please inter correctly phonenumber!!')]
    )
    fullname=models.CharField(max_length=30)
    username=models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(regex='^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$')]
    )
    password=models.CharField(
        max_length=20,
        validators=[RegexValidator(regex='^(?=[^a-z]*[a-z])(?=\D*\d)[^:&.~\s]{5,20}$')]
    )
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD='username'


class Follow(models.Model):
    STATUS_CHOICES=[
        ('accept','Accept'),
        ('pending','Pending')
    ] 
    user=models.CharField(max_length=30)
    followers=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='followers',null=True,blank=True,on_delete=models.CASCADE)
    following=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='followings',null=True,blank=True,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

    def __str__(self) -> str:
        return self.user


# class Follow(models.Model):
#     STATUS_CHOICES=[
#         ('accept','Accept'),
#         ('panding','Panding')
#     ] 

#     follower=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='followers',on_delete=models.CASCADE)
#     following=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='followings',on_delete=models.CASCADE)
#     status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

#     def __str__(self) -> str:
#         return f'{self.follower.username}-{self.following.username}'