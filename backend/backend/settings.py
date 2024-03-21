import os
from datetime import timedelta

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = (
    "django-insecure-zdlmk&^f_o_cd^^qs5fnz2*l5xn%81*iqi8qb!p^5nc0rd@66q"
)

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
    "testserver",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "magic",
    "drf_spectacular",
    "drf_multiple_model",
    "django_filters",
    "mutagen",
    "users.apps.UsersConfig",
    "content.apps.ContentConfig",
    "api.v1.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "current_user": "api.v1.serializers.CustomUserSerializer",
    },
    "PERMISSIONS": {
        "token_create": ["rest_framework.permissions.AllowAny"],
        "create_user": ["rest_framework.permissions.AllowAny"],
        "current_user": ["rest_framework.permissions.IsAuthenticated"],
    },
    "HIDE_USERS": True,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ARTUR'S STORIES API",
    "DESCRIPTION": ("API-Документация для SPA ARTUR'S STORIES."),
    "VERSION": "0.1.0",
    "SCHEMA_PATH_PREFIX": "/api/v1/",
    "SERVE_INCLUDE_SCHEMA": False,
}

QUANTITY_OF_FREE_CONTENT_PER_CLASS = 4
VALID_AUDIO_FORMATS = ["mp3", "wav"]
AGE_CHOICES = (
    ("0-3", "0-3"),
    ("3-6", "3-6"),
    ("7-10", "7-10"),
)
TAGS = (
    ("MORNING", "Утро"),
    ("NOON", "День"),
    ("EVENING", "Вечер"),
)
