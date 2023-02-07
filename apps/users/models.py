from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    supervisor = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)
    patronymic = models.CharField(max_length=30, blank=True)

class Vacations(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_time = models.DateTimeField(auto_now_add=True)
    is_by_schedule = models.BooleanField(null=True)
    startdate = models.DateField()
    finishdate = models.DateField()
    duration = models.IntegerField(null=True)
    supervisor = models.CharField(max_length=30, blank=True)
    jun_hr = models.CharField(max_length=30, blank=True)
    head_hr = models.CharField(max_length=30, blank=True)
    director = models.CharField(max_length=30, blank=True)
    comments = models.CharField(max_length=100, blank=True)