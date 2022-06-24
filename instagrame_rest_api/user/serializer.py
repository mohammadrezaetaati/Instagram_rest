from dataclasses import fields
from pyexpat import model
from webbrowser import get
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Follow


class UserRegisterSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model=get_user_model()
        fields=['fullname','username','phonenumber','password','email']
        extra_kwargs={
            'passwordConfirmation':{'write_only':True},
            'password':{'write_only':True}
        }
        depth=1
       
    def create(self, validated_data):
        password=validated_data.pop('password')
        if password!=self.context['passwordConfirmation']:
            raise ValueError('fc')
        user=get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    username=serializers.StringRelatedField()

    class Meta:
        model=get_user_model()
        fields=['username']

        
class FollowingSerializer(serializers.ModelSerializer):

    following=UserSerializer()
    class Meta:
        model=Follow
        fields=['following']
        

class FollowerSerializer(serializers.ModelSerializer):

    followers=UserSerializer()
    class Meta:
        model=Follow
        fields=['followers']
        
# class FollowSerializer(serializers.Serializer):

#     follow=serializers.CharField()
#     followers=serializers.CharField(read_only=True)
  

#     def create(self, validated_data):
#         """
#         Follower operation
#         """
#         user_follow=get_object_or_404(get_user_model(),username=validated_data.get('follow'))
#         user_login=get_user_model().objects.get(username=self.context['user'])
#         user : Follow=Follow.objects.get_or_create(user=user_login)[0]
#         user.followers.add(user_follow)
#         """
#         following operation
#         """
#         user_following:Follow=Follow.objects.get_or_create(user=user_follow)[0]
#         user_following.following.add(user_login)
#         return validated_data
       


# class UnFollowSerializer(serializers.Serializer):

#     unfollow=serializers.CharField()

#     def create(self, validated_data):
#         user_login=get_user_model().objects.get(username=self.context['user'])
#         user : Follow=Follow.objects.get_or_create(user=user_login)[0]
#         user_follow=get_object_or_404(get_user_model(),username=validated_data.get('unfollow'))
#         user.followers.remove(user_follow)
#         return validated_data
        
# class FollowUserTable(serializers.ModelSerializer):

#     username=serializers.StringRelatedField()
#     class Meta:
#         model=get_user_model()
#         fields=['username']


# class FollowSerializers(serializers.ModelSerializer):
   
   
#     class Meta:
#         model= Follow
#         fields="__all__"
#         extra_kwargs={
#             'status':{'read_only':True},
#             'follower':{'read_only':True},
#         }
     

#     def create(self, validated_data):
#         print('ffffffffffffffffffff')
#         user_login=get_user_model().objects.get(username='ali')  
#         print(Follow.objects.all().values())
#         # print(validated_data['following'])
#         # Follow.objects.create(follower_id=1,following_id=3)
#         # user_login.followings.add(user_login)
#         print(user_login.followings.all())
#         # Follow.objects.create(follower_id=4,following_id=1)
        
#         # print(validated_data['follower'])
#         return validated_data
# class Test(serializers.Serializer):
#     user=serializers.CharField()
        
