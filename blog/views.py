from rest_framework import permissions, generics
from .models import Blog
from .serializers import BlogSerializer


class RetrieveApiView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CreateApiView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminUser]

    # def post(self, request, *args, **kwargs):
    #     print(request.data)

