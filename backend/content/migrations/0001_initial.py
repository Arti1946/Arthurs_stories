# Generated by Django 5.0.2 on 2024-02-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AudioBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=150, verbose_name="Название"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        null=True,
                        unique=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "author",
                    models.CharField(max_length=150, verbose_name="Автор"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата Загрузки"
                    ),
                ),
                (
                    "duration",
                    models.DurationField(verbose_name="Продолжительность"),
                ),
                ("chapter", models.PositiveSmallIntegerField()),
                (
                    "file",
                    models.FileField(
                        upload_to="media/audio_files/Audio Books/",
                        verbose_name="Файл",
                    ),
                ),
            ],
            options={
                "verbose_name": "Аудио книга",
                "verbose_name_plural": "Аудиокниги",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Fairytale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=150, verbose_name="Название"),
                ),
                (
                    "author",
                    models.CharField(
                        max_length=150, verbose_name="Автор произведения"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=500, unique=True, verbose_name="Описание"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("0-3", "0-3"),
                            ("3-6", "3-6"),
                            ("7-10", "7-10"),
                        ],
                        max_length=5,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата загрузки"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="media/audio_files/Fairy tales/",
                        verbose_name="Файл",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(verbose_name="Продолжительность"),
                ),
            ],
            options={
                "verbose_name": "Сказка",
                "verbose_name_plural": "Сказки",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Lullaby",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=150, verbose_name="Название"),
                ),
                (
                    "author",
                    models.CharField(
                        max_length=150, verbose_name="Исполнитель"
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата загрузки"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="media/audio_files/Lullabies/",
                        verbose_name="Файл",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(verbose_name="Продолжительность"),
                ),
            ],
            options={
                "verbose_name": "Колыбельная",
                "verbose_name_plural": "Колыбельные",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Meditation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, unique=True)),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата загрузки"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="media/audio_files/Meditations/",
                        verbose_name="Файл",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(verbose_name="Продолжительность"),
                ),
                (
                    "category",
                    models.CharField(max_length=150, verbose_name="Категория"),
                ),
                (
                    "tags",
                    models.CharField(
                        choices=[
                            ("MORNING", "Утро"),
                            ("NOON", "День"),
                            ("EVENING", "Вечер"),
                        ],
                        max_length=150,
                        verbose_name="Тег",
                    ),
                ),
            ],
            options={
                "verbose_name": "Медитация",
                "verbose_name_plural": "Медитации",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.AddConstraint(
            model_name="audiobook",
            constraint=models.UniqueConstraint(
                fields=("title", "chapter"),
                name="unique_audiobook_title_chapter",
            ),
        ),
        migrations.AddConstraint(
            model_name="fairytale",
            constraint=models.UniqueConstraint(
                fields=("title", "author"),
                name="unique_fairytale_title_author",
            ),
        ),
        migrations.AddConstraint(
            model_name="lullaby",
            constraint=models.UniqueConstraint(
                fields=("title", "author"), name="unique_lullaby_title_author"
            ),
        ),
    ]
