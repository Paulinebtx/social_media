from django.contrib import admin
from .models import posts, postsComment, postsLike

admin.site.register(posts)
admin.site.register(postsComment)
admin.site.register(postsLike)

