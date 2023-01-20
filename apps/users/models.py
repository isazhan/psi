from django.db import models
from django.conf import settings


class Vacations(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    startdate = models.DateField()
    finishdate = models.DateField()
    supervisor = models.BooleanField(null=True)
    jun_hr = models.BooleanField(null=True)
    head_hr = models.BooleanField(null=True)
    director = models.BooleanField(null=True)