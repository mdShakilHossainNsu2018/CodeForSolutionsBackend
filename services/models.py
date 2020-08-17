from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=200)
