import re

from django.core.exceptions import ValidationError

from datetime import date


def validate_username(value):
    regex = re.compile(r"^[\w.@+-]+\Z")
    if not regex.match(value):
        raise ValidationError("Выберите другое имя")
    elif value == "me":
        raise ValidationError("Нельзя выбрать такое имя")


def validate_birth_date(value):
    if value > date.today():
        raise ValidationError("Дата рождения не может быть в будущем")
