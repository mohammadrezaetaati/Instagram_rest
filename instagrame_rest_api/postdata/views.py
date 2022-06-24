from multiprocessing import context
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status

from .models import Post,Comment
from .serializer import Postserializer,CommentSerializer
from user.models import Follow


class PostCrud(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Postserializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        print(self.request.user)
        context['user'] = self.request.user
        return context

def get_user(request):
     return Follow.objects.filter(user = request.user, status = 'accept',).values\
                ('following').exclude(following__isnull=True)

class Home(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        post = Post.objects.filter(user__in=get_user(request))
        serializer = Postserializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'],detail=True,url_path='like')
    def like(self,request,pk):
        try:
            print(get_user(request))
            post :Post = Post.objects.get(user__in=get_user(request),id=pk)
            post.like+=1
            post.save()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'],detail=True,url_path='unlike')
    def unlike(self,request,pk):
        try:
            post :Post = Post.objects.get(user__in=get_user(request),id=pk)
            post.like-=1
            post.save()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'],detail=True,url_path='comment')
    def comment(self,request,pk):
        try:
            post=Post.objects.filter(user__in=get_user(request),id=pk).values_list('id')
            serializer=CommentSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.validated_data.get('text'))
                Comment.objects.create(text = serializer.validated_data.get('text'),post_id = post[0][0])
                return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
  




