from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.v1.serializers import (
    LullabySerializer,
    FairytaleSerializer,
    AudiobookSerializer,
    MeditationSerializer,
)
from content.models import Lullaby, Fairytale, AudioBook, Meditation


class LullabyViewSet(viewsets.ModelViewSet):
    queryset = Lullaby.objects.all()
    serializer_class = LullabySerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get"]


class FairytaleViewSet(viewsets.ModelViewSet):
    queryset = Fairytale.objects.all()
    serializer_class = FairytaleSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get"]


class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudiobookSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get"]


class MeditationViewSet(viewsets.ModelViewSet):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get"]
