from rest_framework import routers

from django.urls import path, include

from api.v1.views import (
    LullabyViewSet,
    AudiobookViewSet,
    FairytaleViewSet,
    MeditationViewSet,
)

router = routers.DefaultRouter()

# router.register(r'users', UserViewSet, basename='users')
router.register(r"lullabies", LullabyViewSet, basename="lullabies")
router.register(r"audiobooks", AudiobookViewSet, basename="audiobooks")
router.register(r"fairytales", FairytaleViewSet, basename="fairytales")
router.register(r"meditations", MeditationViewSet, basename="meditations")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
