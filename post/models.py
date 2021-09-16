from django.db import models
from django.contrib.auth.models import User


class posts(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255, db_index=True, null=True)
    # slug = models.SlugField(max_length=255, unique=True, null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    # img = models.ImageField(upload_to='images_uploaded',null=True, required = False)
    # video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    # date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class postsComment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255, db_index=True, null=True)
    postComment = models.ForeignKey(posts, related_name='postComment', on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class postsLike(models.Model):
    id = models.AutoField(primary_key=True)
    postLike = models.ForeignKey(posts, related_name='postLike', on_delete=models.CASCADE)
    user_like = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.postsLike