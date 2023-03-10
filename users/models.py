from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]
