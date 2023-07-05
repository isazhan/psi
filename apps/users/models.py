from typing import Any, Optional
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.http.request import HttpRequest
from db import get_db_handle
from django.contrib.auth.hashers import check_password, make_password

"""
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
"""

class UserBackend(ModelBackend):

    def authenticate(self, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        print(type(email), type(password))
        try:
            user = get_db_handle()['users'].find_one({'email': email}, {'_id': 0, 'email': 1, 'password': 1})
            print(user)
            #get_db_handle()['users'].update_one({'email': 'u.isazhan@psi-group.kz'}, { '$set': {'password': make_password('123456789')}})
            #if user['password'] == password:

            if check_password(password, user['password']) is True:
                print('right password')
                return user['email']
            else:
                print('wrong password')
                return None
        except:
            return None
    
    def get_user(self, user_id):
        try:
            return get_db_handle()['users'].find_one({'email': user_id})
        except:
            return None