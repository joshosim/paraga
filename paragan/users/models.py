from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(null=False, max_length=50)
    username = models.CharField(null=False, unique=True, max_length=100, db_index=True, blank=False)
    phone_number = models.IntegerField(null=False, unique=True, blank=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['phone_number']
    USERNAME_FIELD = 'username'

    objects = UserManager()

class UserData(models.Model):
    id = models.IntegerField(null=False, db_index=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.IntegerField(unique=True, null=True)