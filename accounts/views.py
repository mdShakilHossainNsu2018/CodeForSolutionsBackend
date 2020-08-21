from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserRegisterSerializer, UserDetailSerializer
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class GetUserByToken(APIView):

    def post(self, request):

        token = request.data.get('token')

        try:
            user = Token.objects.get(key=token).user
        except:
            return Response('user does not exists', status=status.HTTP_204_NO_CONTENT)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



