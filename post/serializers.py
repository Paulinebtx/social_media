from rest_framework import serializers
from .models import posts, postsComment, postsLike


class postsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = posts
        fields = ('__all__')

class postsCommentSerializer(serializers.ModelSerializer):
    user_comment = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = postsComment
        fields = ('__all__')


class postsLikeSerializer(serializers.ModelSerializer):
    user_like = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = postsLike
        fields = ('__all__')