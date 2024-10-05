from django.shortcuts import get_object_or_404
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

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
    NewsSerializer,
    MainSerializer, NewsLullabySerializer,
)
from content.models import Lullaby, Fairytale, AudioBook, Meditation, News
from users.models import (
    FavoriteLullaby,
    FavoriteFairytale,
    FavoriteAudiobook,
    FavoriteMeditation,
)


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 3


@extend_schema(tags=["Главная страница"])
@extend_schema_view(
    get=extend_schema(
        summary="Список контента",
        description="В поле <b><i>News</i></b> содержатся по 2 последние записи со всеми атрибутами от каждой категории контента. Остальные поля отображают только бесплатный контент. </br> Доступно всем пользователям без исключения",
        responses={200: MainSerializer},
        filters=True,
    )
)
class MainAPIView(ObjectMultipleModelAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ("title",)
    permission_classes = [AllowAny]
    http_method_names = ["get"]
    pagination_class = None

    def get_querylist(self):
        news = (
            News(
                lullabies=Lullaby.objects.order_by("-id")[:2],
                fairytales=Fairytale.objects.order_by("-id")[:2],
                meditations=Meditation.objects.order_by("-id")[:2],
                audiobooks=AudioBook.objects.order_by("-id")[:2],
            ),
        )
        free = False
        if self.request.user.is_authenticated and self.request.user.is_premium:
            free = True
        querylist = [
            {
                "queryset": Lullaby.objects.filter(is_free=free).order_by("title")[:3],
                "serializer_class": LullabySerializer,
                "label": "Lullabies",
            },
            {
                "queryset": Fairytale.objects.filter(is_free=free).order_by("title")[:3],
                "serializer_class": FairytaleSerializer,
                "label": "Fairytales",
            },
            {
                "queryset": AudioBook.objects.filter(is_free=free).order_by("title")[:3],
                "serializer_class": AudiobookSerializer,
                "label": "Audiobooks",
            },
            {
                "queryset": Meditation.objects.filter(is_free=free).order_by("title")[:3],
                "serializer_class": MeditationSerializer,
                "label": "Meditations",
            },
            {
                "queryset": news,
                "serializer_class": NewsSerializer,
                "label": "News",
            },
        ]
        if self.request.query_params:
            querylist.pop()
        return querylist


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

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return Lullaby.objects.all()
        return Lullaby.objects.filter(is_free=True)

    def get_serializer_class(self):
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return LullabySerializer
        return NewsLullabySerializer


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
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return Fairytale.objects.all()
        return Fairytale.objects.filter(is_free=True)

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
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return AudioBook.objects.all()
        return AudioBook.objects.filter(is_free=True)

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
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return Meditation.objects.all()
        return Meditation.objects.filter(is_free=True)

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
