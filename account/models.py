from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length = 30)
    status = models.BooleanField(default = 1)

    def __str__(self):
        return self.username