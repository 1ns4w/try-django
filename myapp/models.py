from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)