from django.db.models import TextChoices


class Tags(TextChoices):
    MORNING = "morning", "Утро"
    NOON = "noon", "День"
    EVENING = "evening", "Вечер"


class Ages(TextChoices):
    NEWBORN = "newborn", "Самые маленькие (0-3)"
    BABIES = "babies", "Малыши (3-6)"
    PUPILS = "pupils", "Школьники (7-10)"


class ContentTypes(TextChoices):
    Audiobook = "audiobook", "Аудиокнига"
    Lullaby = "lullaby", "Колыбельная"
    Fairytale = "fairytale", "Сказка"
    Song = "song", "Песня"
    Meditation = "meditation", "Медитация"
