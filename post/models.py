from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255, db_index=True, null=True)
    # slug = models.SlugField(max_length=255, unique=True, null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    # img = models.ImageField(upload_to='images_uploaded',null=True, required = False)
    # video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    # date_uploaded = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.text

class Post_comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255, db_index=True, null=True)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE, null=True)




    def __str__(self):
        return self.text