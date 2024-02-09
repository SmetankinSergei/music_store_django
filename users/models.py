from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/avatars/')
    phone = models.CharField(max_length=35, **NULLABLE)
    country = models.CharField(max_length=50, **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
