from django.db import models

# Create your models here.

class actor(models.Model):
      name = models.CharField(max_length=30, null=True, blank=True,)
      age = models.IntegerField(max_length=40, null=True, blank=True )
      moveis = models.OneToManyField()


class movie(models.Model):
      name = models.CharField(max_length=30, null=True, blank=True,)
      age = models.IntegerField(max_length=40, null=True, blank=True )
