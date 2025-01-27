# Generated by Django 5.0.2 on 2024-10-05 11:31

import django.contrib.auth.models
import django.utils.timezone
import users.models
import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Почта"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=150,
                        unique=True,
                        validators=[users.validators.validate_username],
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="Фамилия"),
                ),
                (
                    "birth_date",
                    models.DateField(
                        validators=[users.validators.validate_birth_date],
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=150, verbose_name="Пароль"),
                ),
                (
                    "is_premium",
                    models.BooleanField(
                        default="False", verbose_name="Оформлена подписка"
                    ),
                ),
                (
                    "user_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=users.models.set_user_pic_path,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["-id"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
