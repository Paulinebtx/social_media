from django.shortcuts import render
from rest_framework import viewsets
from .serializers import postSerializer,post_commentSerializer
from .models import Post, Post_comment


class PostViewsets(viewsets.ModelViewSet):
    serializer_class = postSerializer
    queryset = Post.objects.all()

class Post_commentViewsets(viewsets.ModelViewSet):
    serializer_class = post_commentSerializer
    queryset = Post_comment.objects.all()