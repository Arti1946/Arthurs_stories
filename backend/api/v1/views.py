from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.conf import settings

from api.v1.permissions import FavoritePermission
from api.v1.serializers import (
    LullabySerializer,
    FairytaleSerializer,
    AudiobookSerializer,
    MeditationSerializer,
    FavoriteLullabySerializer,
    FavoriteFairytaleSerializer,
    FavoriteAudiobookSerializer,
    FavoriteMeditationSerializer,
)
from content.models import Lullaby, Fairytale, AudioBook, Meditation
from users.models import (
    FavoriteLullaby,
    FavoriteFairytale,
    FavoriteAudiobook,
    FavoriteMeditation,
)


@extend_schema(tags=["Колыбельные"])
@extend_schema_view(
    list=extend_schema(
        summary="Список колыбельных",
    ),
    retrieve=extend_schema(summary="Колыбельная"),
)
class LullabyViewSet(viewsets.ModelViewSet):
    serializer_class = LullabySerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options", "post", "delete"]
    permission_classes = [FavoritePermission]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        if self.request.user.is_premium:
            return Lullaby.objects.all()
        return Lullaby.objects.filter(
            id__lte=settings.QUANTITY_OF_FREE_CONTENT_PER_CLASS
        )

    @extend_schema(
        summary="Избранное",
        description=(
            "Добавление или удаление  колыбельной из избранного посредство методов POST, DELETE"
        ),
    )
    @action(
        detail=True,
        methods=["post", "delete"],
    )
    def favorite(self, request, pk):
        user = request.user
        if request.method == "POST":
            if not FavoriteLullaby.objects.filter(
                users=user, lullabies=pk
            ).exists():
                lullaby = get_object_or_404(Lullaby, pk=pk)
                serializer = FavoriteLullabySerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(users=user, lullabies=lullaby)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                "Колыбельная уже в избранном",
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            FavoriteLullaby.objects.filter(users=user, lullabies=pk).delete()[
                0
            ]
            == 0
        ):
            return Response(
                "Колыбельной нет в избранном",
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            "Колыбельная удалена из избранного",
            status=status.HTTP_204_NO_CONTENT,
        )


@extend_schema(tags=["Сказки"])
@extend_schema_view(
    list=extend_schema(
        summary="Список Сказок",
    ),
    retrieve=extend_schema(summary="Сказка"),
)
class FairytaleViewSet(viewsets.ModelViewSet):
    serializer_class = FairytaleSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options", "post", "delete"]
    permission_classes = [FavoritePermission]

    def get_queryset(self):
        if self.request.user.is_premium:
            return Fairytale.objects.all()
        return Fairytale.objects.filter(
            id__lte=settings.QUANTITY_OF_FREE_CONTENT_PER_CLASS
        )

    @extend_schema(
        summary="Избранное",
        description=(
            "Добавление или удаление сказки из избранного посредство методов POST, DELETE"
        ),
    )
    @action(
        detail=True,
        methods=["post", "delete"],
    )
    def favorite(self, request, pk):
        user = request.user
        if request.method == "POST":
            if not FavoriteFairytale.objects.filter(
                users=user, fairytales=pk
            ).exists():
                fairytale = get_object_or_404(Fairytale, pk=pk)
                serializer = FavoriteFairytaleSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(users=user, fairytales=fairytale)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                "Сказка уже в избранном", status=status.HTTP_400_BAD_REQUEST
            )
        if (
            FavoriteFairytale.objects.filter(
                users=user, fairytales=pk
            ).delete()[0]
            == 0
        ):
            return Response(
                "Сказки нет в избранном", status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            "Сказка удалена из избранного", status=status.HTTP_204_NO_CONTENT
        )


@extend_schema(tags=["Аудиокниги"])
@extend_schema_view(
    list=extend_schema(
        summary="Список аудиокниг",
    ),
    retrieve=extend_schema(summary="Аудиокнига"),
)
class AudiobookViewSet(viewsets.ModelViewSet):
    serializer_class = AudiobookSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options", "post", "delete"]
    permission_classes = [FavoritePermission]

    def get_queryset(self):
        if self.request.user.is_premium:
            return AudioBook.objects.all()
        return AudioBook.objects.filter(
            id__lte=settings.QUANTITY_OF_FREE_CONTENT_PER_CLASS
        )

    @extend_schema(
        summary="Избранное",
        description=(
            "Добавление или удаление аудиокниги из избранного посредство методов POST, DELETE"
        ),
    )
    @action(
        detail=True,
        methods=["post", "delete"],
    )
    def favorite(self, request, pk):
        user = request.user
        if request.method == "POST":
            if not FavoriteAudiobook.objects.filter(
                users=user, audiobooks=pk
            ).exists():
                audiobook = get_object_or_404(AudioBook, pk=pk)
                serializer = FavoriteAudiobookSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(users=user, audiobooks=audiobook)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                "Аудиокнига уже в избранном",
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            FavoriteAudiobook.objects.filter(
                users=user, audiobooks=pk
            ).delete()[0]
            == 0
        ):
            return Response(
                "Аудиокниги нет в избранном",
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            "Аудиокнига удалена из избранного",
            status=status.HTTP_204_NO_CONTENT,
        )


@extend_schema(tags=["Медитации"])
@extend_schema_view(
    list=extend_schema(
        summary="Список медитаций",
    ),
    retrieve=extend_schema(summary="Медитация"),
)
class MeditationViewSet(viewsets.ModelViewSet):
    serializer_class = MeditationSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options", "post", "delete"]
    permission_classes = [FavoritePermission]

    def get_queryset(self):
        if self.request.user.is_premium:
            return Meditation.objects.all()
        return Meditation.objects.filter(
            id__lte=settings.QUANTITY_OF_FREE_CONTENT_PER_CLASS
        )

    @extend_schema(
        summary="Избранное",
        description=(
            "Добавление или удаление медитации из избранного посредство методов POST, DELETE"
        ),
    )
    @action(
        detail=True,
        methods=["post", "delete"],
    )
    def favorite(self, request, pk):
        user = request.user
        if request.method == "POST":
            if not FavoriteMeditation.objects.filter(
                user=user, meditations=pk
            ).exists():
                meditation = get_object_or_404(Meditation, pk=pk)
                serializer = FavoriteMeditationSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(users=user, meditations=meditation)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                "Медитация уже в избранном", status=status.HTTP_400_BAD_REQUEST
            )
        if (
            FavoriteMeditation.objects.filter(
                users=user, meditations=pk
            ).delete()[0]
            == 0
        ):
            return Response(
                "Медитации нет в избранном", status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            "Медитация удалена из избранного",
            status=status.HTTP_204_NO_CONTENT,
        )
