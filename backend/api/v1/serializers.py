from djoser.serializers import UserSerializer
from rest_framework import serializers

from content.models import (
    Lullaby,
    AudioBook,
    Fairytale,
    Meditation,
)
from users.models import (
    CustomUser,
    FavoriteFairytale,
    FavoriteAudiobook,
    FavoriteLullaby,
    FavoriteMeditation,
)


class LullabySerializer(serializers.ModelSerializer):
    duration = serializers.TimeField(format='%M:%S')

    class Meta:
        model = Lullaby
        fields = ("title", "author", "duration", "pub_date", "file")


class NewsLullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = ("title", "author", "duration", "pub_date")


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ("title", "chapter", "author", "description", "duration", "pub_date", "file")


class NewsAudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ("title", "chapter", "author", "description", "duration", "pub_date")



class FairytaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = ("title", "author", "category", "duration", "pub_date", "file")


class NewsFairytaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = ("title", "author", "category", "duration", "pub_date")


class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ("title", "category", "tags", "duration", "pub_date", "file")


class NewsMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ("title", "category", "tags", "duration", "pub_date")


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
    lullabies = NewsLullabySerializer(many=True)
    audiobooks = NewsAudiobookSerializer(many=True)
    meditations = NewsMeditationSerializer(many=True)
    fairytales = NewsFairytaleSerializer(many=True)


class MainSerializer(serializers.Serializer):
    news = NewsSerializer(many=True)
    lullabies = LullabySerializer(many=True)
    fairytales = FairytaleSerializer(many=True)
    audiobooks = AudiobookSerializer(many=True)
    meditations = MeditationSerializer(many=True)
