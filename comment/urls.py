from .views import CreateOrRetrieveApiView
from django.urls import path


urlpatterns = [
    path('', CreateOrRetrieveApiView.as_view()),
]