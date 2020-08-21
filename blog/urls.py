from .views import RetrieveApiView, CreateApiView
from django.urls import path


urlpatterns = [
    path('', RetrieveApiView.as_view()),
    path('create/', CreateApiView.as_view()),
]
