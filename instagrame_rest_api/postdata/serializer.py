
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Post,Comment
from user.serializer import UserSerializer




class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Comment
        fields=['text']


class Postserializer(serializers.ModelSerializer):
    comment=serializers.SerializerMethodField(read_only=True)
    user=UserSerializer(read_only=True)
    class Meta:
        model=Post
        fields=['id','user','caption','img','like','comment','create_at','update_at']
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data,user=self.context['user'])
     
        
    def get_comment(self,obj):
        comment=Comment.objects.filter(post=obj)
        serializer=CommentSerializer(comment,many=True)
        return serializer.data

        

