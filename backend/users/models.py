from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

from .validators import validate_username
from content.models import Fairytale, Meditation, AudioBook, Lullaby


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
    age = models.PositiveSmallIntegerField("Возраст", null=False, blank=False)
    password = models.CharField(
        "Пароль", max_length=150, blank=False, null=False
    )
    is_premium = models.BooleanField("Оформлена подписка", default="False")
    favorite_fairytales = models.ManyToManyField(
        Fairytale,
        through="Favorite",
        through_fields=("users", "fairytales"),
        related_name="fairytales",
        verbose_name="Избранные сказки",
    )
    favorite_audiobooks = models.ManyToManyField(
        AudioBook,
        through="Favorite",
        through_fields=("users", "audiobooks"),
        related_name="audiobooks",
        verbose_name="Избранные аудиокниги",
    )
    favorite_lullabies = models.ManyToManyField(
        Lullaby,
        through="Favorite",
        through_fields=("users", "lullabies"),
        related_name="lullabies",
        verbose_name="Избранные колыбельные",
    )
    favorite_meditations = models.ManyToManyField(
        Meditation,
        through="Favorite",
        through_fields=("users", "meditations"),
        related_name="meditations",
        verbose_name="Избранные медитации",
    )
    user_pic = models.ImageField(
        blank=True, null=True, upload_to=set_user_pic_path
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "password",
        "age",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.username


class Favorite(models.Model):
    users = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name="Пользователь",
    )
    fairytales = models.ForeignKey(
        Fairytale,
        related_name="favorite_fairytales",
        on_delete=models.SET_NULL,
        verbose_name="Избранные сказки",
        null=True,
        blank=True,
    )
    lullabies = models.ForeignKey(
        Lullaby,
        related_name="favorite_lullabies",
        on_delete=models.SET_NULL,
        verbose_name="Избранные колыбельные",
        null=True,
        blank=True,
    )
    meditations = models.ForeignKey(
        Meditation,
        related_name="favorite_meditations",
        on_delete=models.SET_NULL,
        verbose_name="Избранные медитации",
        null=True,
        blank=True,
    )
    audiobooks = models.ForeignKey(
        AudioBook,
        related_name="favorite_audiobooks",
        on_delete=models.SET_NULL,
        verbose_name="Избранные аудиокниги",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = ("Избранное",)
        verbose_name_plural = "Избранные"
        unique_together = (
            ("users", "audiobooks"),
            ("users", "lullabies"),
            ("users", "meditations"),
            ("users", "fairytales"),
        )

    def __str__(self):
        return f"{self.users} {self.lullabies} {self.fairytales} {self.meditations} {self.audiobooks}"
