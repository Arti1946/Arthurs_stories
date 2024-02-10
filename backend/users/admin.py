from django.contrib import admin

from users.models import CustomUser, Favorite


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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related(
            "favorite_audiobooks",
            "favorite_lullabies",
            "favorite_meditations",
            "favorite_fairytales",
        )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "users",
        "lullabies",
        "fairytales",
        "audiobooks",
        "meditations",
    )
    list_filter = (
        "audiobooks",
        "lullabies",
        "meditations",
        "fairytales",
    )
    search_fields = ("users",)
