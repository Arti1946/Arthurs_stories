from datetime import date

from django.contrib import admin

from users.models import (
    CustomUser,
    FavoriteLullaby,
    FavoriteAudiobook,
    FavoriteMeditation,
    FavoriteFairytale,
)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "age",
        "is_premium",
    )
    ordering = ("-id",)
    search_fields = ("username", "first_name", "last_name", "email")

    @admin.display(description="age")
    def age(self, user):
        birth_date = user.birth_date
        today_date = date.today()
        age = today_date - birth_date
        return age.days // 365

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related(
            "favorite_audiobooks",
            "favorite_lullabies",
            "favorite_meditations",
            "favorite_fairytales",
        )


@admin.register(FavoriteLullaby)
class FavoriteLullabyAdmin(admin.ModelAdmin):
    list_display = (
        "users",
        "lullabies",
    )
    list_filter = (
        "users",
        "lullabies",
    )
    search_fields = ("users", "lullabies")
    list_editable = ("lullabies",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("users", "lullabies")


@admin.register(FavoriteAudiobook)
class FavoriteAudiobooksAdmin(admin.ModelAdmin):
    list_display = (
        "users",
        "audiobooks",
    )
    list_filter = (
        "users",
        "audiobooks",
    )
    search_fields = ("users", "audiobooks")
    list_editable = ("audiobooks",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("users", "audiobooks")


@admin.register(FavoriteMeditation)
class FavoriteMeditationAdmin(admin.ModelAdmin):
    list_display = (
        "users",
        "meditations",
    )
    list_filter = ("meditations", "users")
    search_fields = ("meditations", "users")
    list_editable = ("meditations",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("users", "meditations")


@admin.register(FavoriteFairytale)
class FavoriteFairytaleAdmin(admin.ModelAdmin):
    list_display = ("users", "fairytales")
    list_filter = ("users", "fairytales")
    search_fields = ("users", "fairytales")
    list_editable = ("fairytales",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("users", "fairytales")
