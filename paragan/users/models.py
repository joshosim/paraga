from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, db_index=True)
    username = models.CharField(max_length=150, unique=True, null=True, db_index=True)
    phone_number = models.IntegerField(null=False, unique=True, blank=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(default=None, null=True)


    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = UserManager()

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=50000)
    user_status = models.CharField(null=True, max_length=5000)
    user_notification = models.CharField(null=True, max_length=3000)
    dedicated_virtual_account = models.CharField(null=True, blank=True, max_length = 100000)
    ref_balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=50000)
    admin = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user.username)