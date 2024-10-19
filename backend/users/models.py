from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_username, validate_birth_date


def set_user_pic_path(instance, filename):
    path = f"users_pics/{instance.username}/{filename}"
    return path


class CustomUser(AbstractUser):
    email = models.EmailField("Почта", unique=True, max_length=254)
    username = models.CharField(
        max_length=150, unique=True, validators=[validate_username]
    )
    first_name = models.CharField(
        "Имя", max_length=150, blank=False, null=False
    )
    last_name = models.CharField(
        "Фамилия", max_length=150, blank=False, null=False
    )
    birth_date = models.DateField(
        "Дата рождения", validators=[validate_birth_date]
    )
    password = models.CharField(
        "Пароль", max_length=150, blank=False, null=False
    )
    is_premium = models.BooleanField("Оформлена подписка", default="False")
    user_pic = models.ImageField(
        blank=True, null=True, upload_to=set_user_pic_path
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "password",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.username
