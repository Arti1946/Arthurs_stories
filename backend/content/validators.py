from mutagen import File

from rest_framework.exceptions import ValidationError

from django.conf import settings


def validate_file_type(upload):
    file_type = File(upload.file).mime[0].strip("audio/")
    if file_type not in settings.VALID_AUDIO_FORMATS:
        raise ValidationError(
            f"Формат {file_type} файла не поддерживается. Рекомендуемые форматы: {settings.VALID_AUDIO_FORMATS}"
        )
