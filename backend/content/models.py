from content import choises
from django.db import models
from django.db.models import UniqueConstraint

from content.validators import validate_file_type

from collections import namedtuple


News = namedtuple(
    "News", ("lullabies", "fairytales", "audiobooks", "meditations")
)


def set_path_name(instance, filename):
    path = instance.__class__.__name__
    return f"audio_files/{path}s/{filename}"


class ContentInfo(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    pub_date = models.DateField(
        auto_now_add=True, verbose_name="Дата загрузки"
    )
    file = models.FileField(
        upload_to=set_path_name,
        null=False,
        blank=False,
        verbose_name="Файл",
        validators=[validate_file_type],
    )
    duration = models.TimeField(
        verbose_name="Продолжительность", null=True, blank=True
    )
    is_free = models.BooleanField(verbose_name="Бесплатный контент")

    class Meta:
        abstract = True


class Fairytale(ContentInfo):
    author = models.CharField(
        max_length=150, verbose_name="Автор произведения"
    )
    description = models.TextField(
        max_length=500, verbose_name="Описание", unique=True
    )
    category = models.CharField(
        max_length=150, choices=choises.Ages, verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Сказка"
        verbose_name_plural = "Сказки"
        ordering = ["-pub_date"]
        constraints = [
            UniqueConstraint(
                fields=("title", "author"),
                name="unique_fairytale_title_author",
            )
        ]

    def __str__(self):
        return self.title


class Lullaby(ContentInfo):
    author = models.CharField(max_length=150, verbose_name="Исполнитель")

    class Meta:
        verbose_name = "Колыбельная"
        verbose_name_plural = "Колыбельные"
        ordering = ["-pub_date"]
        constraints = [
            UniqueConstraint(
                fields=("title", "author"),
                name="unique_lullaby_title_author",
            )
        ]

    def __str__(self):
        return self.title


class AudioBook(ContentInfo):
    description = models.TextField(
        verbose_name="Описание", null=True, blank=True, unique=True
    )
    author = models.CharField(max_length=150, verbose_name="Автор")
    chapter = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Глава"
    )

    class Meta:
        verbose_name = "Аудио книга"
        verbose_name_plural = "Аудиокниги"
        ordering = ["-pub_date"]
        constraints = [
            UniqueConstraint(
                fields=("title", "chapter"),
                name="unique_audiobook_title_chapter",
            )
        ]

    def __str__(self):
        return self.title


class Meditation(ContentInfo):
    category = models.CharField(max_length=150, verbose_name="Категория")
    tags = models.CharField(
        max_length=150, choices=choises.Tags, verbose_name="Тег"
    )

    class Meta:
        verbose_name = "Медитация"
        verbose_name_plural = "Медитации"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title
