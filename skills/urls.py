from django.urls import path
from .views import SkillApiView

urlpatterns = [
    path('', SkillApiView.as_view()),
]