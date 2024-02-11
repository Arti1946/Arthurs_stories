import magic
from rest_framework.exceptions import ValidationError

from django.conf import settings


def validate_file_type(upload):
    file_type = magic.from_buffer(upload.file.read(1024), mime=True)
    if file_type not in settings.VALID_AUDIO_FORMATS:
        raise ValidationError(
            f"Формат файла не поддерживается./n Рекомендуемые форматы: {settings.VALID_AUDIO_FORMATS}"
        )
