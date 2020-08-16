from rest_framework import generics
from .serializers import SkillSerializer
from .models import Skill


class SkillApiView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
