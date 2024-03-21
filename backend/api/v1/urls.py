from rest_framework import routers

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from api.v1.views import (
    LullabyViewSet,
    AudiobookViewSet,
    FairytaleViewSet,
    MeditationViewSet,
    MainAPIView,
)

router = routers.DefaultRouter()
router.register(r"lullabies", LullabyViewSet, basename="lullabies")
router.register(r"audiobooks", AudiobookViewSet, basename="audiobooks")
router.register(r"fairytales", FairytaleViewSet, basename="fairytales")
router.register(r"meditations", MeditationViewSet, basename="meditations")


urlpatterns = [
    path("", include(router.urls)),
    path("main/", MainAPIView.as_view(), name="main"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
