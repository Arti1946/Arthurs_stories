# Generated by Django 5.0.2 on 2024-02-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "content",
            "0002_alter_audiobook_duration_alter_fairytale_duration_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="meditation",
            name="duration",
            field=models.TimeField(
                blank=True, null=True, verbose_name="Продолжительность"
            ),
        ),
    ]
