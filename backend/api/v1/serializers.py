from djoser.serializers import UserSerializer
from rest_framework import serializers

from content.models import (
    Lullaby,
    AudioBook,
    Fairytale,
    Meditation,
    ContentInfo,
    News,
)
from users.models import (
    CustomUser,
    FavoriteFairytale,
    FavoriteAudiobook,
    FavoriteLullaby,
    FavoriteMeditation,
)


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = "__all__"


class FairytaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = "__all__"


class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = "__all__"


class CustomUserSerializer(UserSerializer):
    favorite_lullabies = LullabySerializer(many=True, read_only=True)
    favorite_audiobooks = AudiobookSerializer(many=True, read_only=True)
    favorite_meditations = MeditationSerializer(many=True, read_only=True)
    favorite_fairytales = FairytaleSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "username",
            "first_name",
            "last_name",
            "favorite_lullabies",
            "favorite_audiobooks",
            "favorite_fairytales",
            "favorite_meditations",
            "birth_date",
        )
        model = CustomUser


class FavoriteFairytaleSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=False, read_only=True)
    fairytales = FairytaleSerializer(many=False, read_only=True)

    class Meta:
        fields = ("users", "fairytales")
        model = FavoriteFairytale


class FavoriteLullabySerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(read_only=True, many=False)
    lullabies = LullabySerializer(read_only=True, many=False)

    class Meta:
        fields = ("users", "lullabies")
        model = FavoriteLullaby


class FavoriteAudiobookSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(read_only=True, many=False)
    audiobooks = AudiobookSerializer(read_only=True, many=False)

    class Meta:
        fields = ("users", "audiobooks")
        model = FavoriteAudiobook


class FavoriteMeditationSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=False, read_only=True)
    meditations = MeditationSerializer(many=False, read_only=True)

    class Meta:
        fields = ("meditations", "users")
        model = FavoriteMeditation


class NewsSerializer(serializers.Serializer):
    lullabies = LullabySerializer(many=True)
    audiobooks = AudiobookSerializer(many=True)
    meditations = MeditationSerializer(many=True)
    fairytales = FairytaleSerializer(many=True)


class MainSerializer(serializers.Serializer):
    news = NewsSerializer(many=True)
    lullabies = LullabySerializer(many=True)
    fairytales = FairytaleSerializer(many=True)
    audiobooks = AudiobookSerializer(many=True)
    meditations = MeditationSerializer(many=True)
