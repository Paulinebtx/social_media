from django.shortcuts import render
from rest_framework import viewsets
from .serializers import postsSerializer, postsCommentSerializer, postsLikeSerializer
from .models import posts, postsComment, postsLike


class postsViewsets(viewsets.ModelViewSet):
    serializer_class = postsSerializer
    queryset = posts.objects.all()

class postsCommentViewsets(viewsets.ModelViewSet):
    serializer_class = postsCommentSerializer
    queryset = postsComment.objects.all()

class postsLikeViewsets(viewsets.ModelViewSet):
    serializer_class = postsLikeSerializer
    queryset = postsLike.objects.all()