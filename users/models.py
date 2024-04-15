from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name="Номер телефона")
    avatar = models.ImageField(
        upload_to="users/avatar/", blank=True, null=True, verbose_name="Аватар"
    )
    country = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Страна"
    )
    token = models.CharField(max_length=50, verbose_name="Токен")

    email = models.EmailField(unique=True, verbose_name="Email")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("is_active", "Активация пользователя")
        ]
