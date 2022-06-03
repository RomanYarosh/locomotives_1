from django.contrib import admin
from . import models


class Locomotive(models.Model):
    locomotive_name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    locomotive_length = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)



