from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'parent', 'owner', 'owner_id', 'blog', 'comment', 'timestamp']