from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

from .validators import validate_username, validate_birth_date
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
    birth_date = models.DateField(
        "Дата рождения", validators=[validate_birth_date]
    )
    password = models.CharField(
        "Пароль", max_length=150, blank=False, null=False
    )
    is_premium = models.BooleanField("Оформлена подписка", default="False")
    favorite_fairytales = models.ManyToManyField(
        Fairytale,
        through="FavoriteFairytale",
        through_fields=("users", "fairytales"),
        related_name="users",
        verbose_name="Избранные сказки",
    )
    favorite_audiobooks = models.ManyToManyField(
        AudioBook,
        through="FavoriteAudiobook",
        through_fields=("users", "audiobooks"),
        related_name="users",
        verbose_name="Избранные аудиокниги",
    )
    favorite_lullabies = models.ManyToManyField(
        Lullaby,
        through="FavoriteLullaby",
        through_fields=("users", "lullabies"),
        related_name="users",
        verbose_name="Избранные колыбельные",
    )
    favorite_meditations = models.ManyToManyField(
        Meditation,
        through="FavoriteMeditation",
        through_fields=("users", "meditations"),
        related_name="users",
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
        "birth_date",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.username


class FavoriteFairytale(models.Model):
    users = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="fairytales",
        verbose_name="Пользователи",
    )
    fairytales = models.ForeignKey(
        Fairytale,
        related_name="fairytales",
        on_delete=models.CASCADE,
        verbose_name="Сказки",
    )

    class Meta:
        verbose_name = ("Избранная сказка",)
        verbose_name_plural = "Избранные сказки"
        constraints = [
            UniqueConstraint(
                fields=("users", "fairytales"),
                name="unique_users_fairytales",
            )
        ]
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.users} {self.fairytales}"


class FavoriteLullaby(models.Model):
    users = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="lullabies",
        verbose_name="Пользователи",
    )
    lullabies = models.ForeignKey(
        Lullaby,
        related_name="lullabies",
        on_delete=models.CASCADE,
        verbose_name="Колыбельные",
    )

    class Meta:
        verbose_name = "Избранная колыбельная"
        verbose_name_plural = "Избранные колыбельные"
        constraints = [
            UniqueConstraint(
                fields=("users", "lullabies"), name="unique_users_lullabies"
            )
        ]
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.users} {self.lullabies}"


class FavoriteMeditation(models.Model):
    users = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="meditations",
        verbose_name="Пользователи",
    )
    meditations = models.ForeignKey(
        Meditation,
        related_name="meditations",
        on_delete=models.CASCADE,
        verbose_name="Медитации",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Избранная медитация"
        verbose_name_plural = "Избранные медитации"
        constraints = [
            UniqueConstraint(
                fields=("users", "meditations"),
                name="unique_users_meditations",
            )
        ]
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.users} {self.meditations}"


class FavoriteAudiobook(models.Model):
    users = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="audiobooks",
        verbose_name="Пользователи",
    )
    audiobooks = models.ForeignKey(
        AudioBook,
        related_name="audiobooks",
        on_delete=models.SET_NULL,
        verbose_name="Аудиокниги",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = ("Избранная аудиокнига",)
        verbose_name_plural = "Избранные аудиокниги"
        constraints = [
            UniqueConstraint(
                fields=("users", "audiobooks"),
                name="unique_users_audiobooks",
            )
        ]
        ordering = ["-id"]

    def __str__(self):
        return f"{self.users} {self.audiobooks}"
