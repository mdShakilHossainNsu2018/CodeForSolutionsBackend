from django.db import models
from django.contrib.auth import get_user_model
from blog.models import Blog
# Create your models here.
User = get_user_model()


class Comment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
