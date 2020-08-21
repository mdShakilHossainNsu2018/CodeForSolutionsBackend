from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


class CreateOrRetrieveApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

