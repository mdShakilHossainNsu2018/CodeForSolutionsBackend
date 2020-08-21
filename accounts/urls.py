from .views import UserListApiView, UserDetailApiView, UserCreateAPIView, GetUserByToken
from django.urls import path

urlpatterns = [
    path('', UserListApiView.as_view()),
    path('user-by-token/', GetUserByToken.as_view()),
    path('<int:pk>/', UserDetailApiView.as_view()),
    path('register/', UserCreateAPIView.as_view()),

]
