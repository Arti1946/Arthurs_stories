from djoser.serializers import UserSerializer
from rest_framework import serializers

from content.models import Content
from users.models import CustomUser


class ContentSerializer(serializers.ModelSerializer):
    duration = serializers.TimeField(format="%H:%M")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            key: value
            for key, value in representation.items()
            if value is not None
        }

    class Meta:
        model = Content
        fields = (
            "id",
            "title",
            "content_type",
            "author",
            "description",
            "category",
            "chapter",
            "tags",
            "duration",
            "pub_date",
            "file",
            "is_free",
        )


class CustomUserSerializer(UserSerializer):
    class Meta:
        fields = (
            "username",
            "first_name",
            "last_name",
            "birth_date",
        )
        model = CustomUser
