from rest_framework import serializers
from .models import Blog
from comment.serializers import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, required=False)

    class Meta:
        model = Blog
        fields = ['id', 'owner', 'blog', 'comment_set', 'timestamp']
