# Generated by Django 5.0.2 on 2024-02-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_customuser_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_pic",
            field=models.ImageField(
                blank=True, null=True, upload_to="Users_pics"
            ),
        ),
    ]
