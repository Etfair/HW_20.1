from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.TextField(verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []