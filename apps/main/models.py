from django.db import models
from django.conf import settings


class Projects(models.Model):
    number = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=150, blank=True)
    customer = models.CharField(max_length=150, blank=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, blank=True)

# Create your models here.
