from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from accounts.managers import UserManager
from . import constants as user_constants

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="user_profile")
    email = models.EmailField(unique=True, null=True, db_index=True)
    phone = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.user.email