from rest_framework import serializers
from .models import Post, Post_comment


class postSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')

class post_commentSerializer(serializers.ModelSerializer):
    user2 = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Post_comment
        fields = ('__all__')