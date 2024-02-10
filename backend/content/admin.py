from django.contrib import admin

from content.models import Fairytale, Lullaby, AudioBook, Meditation


@admin.register(Fairytale)
class FairytaleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "description",
        "category",
        "pub_date",
        "file",
        "duration",
    )
    list_editable = (
        "title",
        "author",
        "description",
        "category",
        "file",
    )
    list_filter = (
        "title",
        "author",
        "category",
        "pub_date",
    )
    search_fields = (
        "title",
        "author",
        "category",
    )
    ordering = ("-pub_date",)


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "pub_date",
        "file",
        "duration",
    )
    list_editable = (
        "title",
        "author",
        "file",
    )
    search_fields = (
        "title",
        "author",
    )
    ordering = ("-pub_date",)
    list_filter = (
        "title",
        "author",
        "pub_date",
    )


@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "description",
        "pub_date",
        "file",
        "duration",
        "chapter",
    )
    list_editable = (
        "title",
        "author",
        "description",
        "file",
        "chapter",
    )
    list_filter = (
        "title",
        "author",
        "pub_date",
    )
    ordering = ("-pub_date",)
    search_fields = (
        "author",
        "title",
    )


@admin.register(Meditation)
class MeditationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "pub_date",
        "file",
        "duration",
        "tags",
    )
    list_editable = (
        "title",
        "tags",
        "category",
        "file",
    )
    list_filter = (
        "title",
        "category",
        "pub_date",
        "tags",
    )
    ordering = ("-pub_date",)
    search_fields = ("title",)
