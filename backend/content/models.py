from content import choises
from django.db import models
from django.db.models import UniqueConstraint

from content.validators import validate_file_type


def set_path_name(instance, filename):
    path = instance.content_type
    return f"audio_files/{path}s/{filename}"


class Content(models.Model):
    content_type = models.CharField(
        "Тип контента",
        choices=choises.ContentTypes,
        blank=False,
        null=False,
        max_length=100,
    )
    title = models.CharField(max_length=150, verbose_name="Название")
    author = models.CharField(
        max_length=150, verbose_name="Автор произведения"
    )
    description = models.TextField(
        max_length=500, verbose_name="Описание", unique=True
    )
    category = models.CharField(
        max_length=150,
        choices=choises.Ages,
        verbose_name="Категория",
        blank=True,
        null=True,
    )
    chapter = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Глава"
    )
    tags = models.CharField(
        max_length=150,
        choices=choises.Tags,
        verbose_name="Тег",
        blank=True,
        null=True,
    )
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
        verbose_name = "Контент"
        verbose_name_plural = "Контент"
        ordering = ["-pub_date"]
        constraints = [
            UniqueConstraint(
                fields=("title", "author", "chapter"),
                name="unique_fairytale_title_author_chapter",
            )
        ]

    def __str__(self):
        return self.title
