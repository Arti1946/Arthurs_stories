# Generated by Django 5.0.2 on 2024-02-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0007_alter_audiobook_file_alter_fairytale_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiobook",
            name="file",
            field=models.FileField(
                upload_to="audio_files/<self.__class__.name>",
                verbose_name="Файл",
            ),
        ),
        migrations.AlterField(
            model_name="fairytale",
            name="file",
            field=models.FileField(
                upload_to="audio_files/<self.__class__.name>",
                verbose_name="Файл",
            ),
        ),
        migrations.AlterField(
            model_name="lullaby",
            name="file",
            field=models.FileField(
                upload_to="audio_files/<self.__class__.name>",
                verbose_name="Файл",
            ),
        ),
        migrations.AlterField(
            model_name="meditation",
            name="file",
            field=models.FileField(
                upload_to="audio_files/<self.__class__.name>",
                verbose_name="Файл",
            ),
        ),
    ]