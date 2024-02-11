# Generated by Django 5.0.2 on 2024-02-11 14:15

import datetime
import django.db.models.deletion
import users.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0009_alter_audiobook_file_alter_fairytale_file_and_more"),
        (
            "users",
            "0005_alter_favorite_audiobooks_alter_favorite_fairytales_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="age",
        ),
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(
                default=datetime.date(2024, 2, 11),
                validators=[users.validators.validate_birth_date],
                verbose_name="Дата рождения",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="FavoriteAudiobook",
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
                    "audiobooks",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="audiobooks",
                        to="content.audiobook",
                        verbose_name="Аудиокниги",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="audiobooks",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Избранная аудиокнига",),
                "verbose_name_plural": "Избранные аудиокниги",
                "ordering": ["-id"],
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="favorite_audiobooks",
            field=models.ManyToManyField(
                related_name="users",
                through="users.FavoriteAudiobook",
                to="content.audiobook",
                verbose_name="Избранные аудиокниги",
            ),
        ),
        migrations.CreateModel(
            name="FavoriteFairytale",
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
                    "fairytales",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fairytales",
                        to="content.fairytale",
                        verbose_name="Сказки",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fairytales",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Избранная сказка",),
                "verbose_name_plural": "Избранные сказки",
                "ordering": ["-id"],
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="favorite_fairytales",
            field=models.ManyToManyField(
                related_name="users",
                through="users.FavoriteFairytale",
                to="content.fairytale",
                verbose_name="Избранные сказки",
            ),
        ),
        migrations.CreateModel(
            name="FavoriteLullaby",
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
                    "lullabies",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lullabies",
                        to="content.lullaby",
                        verbose_name="Колыбельные",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lullabies",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранная колыбельная",
                "verbose_name_plural": "Избранные колыбельные",
                "ordering": ["-id"],
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="favorite_lullabies",
            field=models.ManyToManyField(
                related_name="users",
                through="users.FavoriteLullaby",
                to="content.lullaby",
                verbose_name="Избранные колыбельные",
            ),
        ),
        migrations.CreateModel(
            name="FavoriteMeditation",
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
                    "meditations",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meditations",
                        to="content.meditation",
                        verbose_name="Медитации",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meditations",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранная медитация",
                "verbose_name_plural": "Избранные медитации",
                "ordering": ["-id"],
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="favorite_meditations",
            field=models.ManyToManyField(
                related_name="users",
                through="users.FavoriteMeditation",
                to="content.meditation",
                verbose_name="Избранные медитации",
            ),
        ),
        migrations.DeleteModel(
            name="Favorite",
        ),
        migrations.AddConstraint(
            model_name="favoriteaudiobook",
            constraint=models.UniqueConstraint(
                fields=("users", "audiobooks"), name="unique_users_audiobooks"
            ),
        ),
        migrations.AddConstraint(
            model_name="favoritefairytale",
            constraint=models.UniqueConstraint(
                fields=("users", "fairytales"), name="unique_users_fairytales"
            ),
        ),
        migrations.AddConstraint(
            model_name="favoritelullaby",
            constraint=models.UniqueConstraint(
                fields=("users", "lullabies"), name="unique_users_lullabies"
            ),
        ),
        migrations.AddConstraint(
            model_name="favoritemeditation",
            constraint=models.UniqueConstraint(
                fields=("users", "meditations"),
                name="unique_users_meditations",
            ),
        ),
    ]
