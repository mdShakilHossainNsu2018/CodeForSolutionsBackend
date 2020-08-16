from django.db import models


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.IntegerField(blank=True, max_length=100)
