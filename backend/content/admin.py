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
        "is_free",
    )
    list_editable = (
        "title",
        "author",
        "description",
        "category",
        "file",
        "is_free",
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
    readonly_fields = ["duration"]


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "pub_date",
        "file",
        "duration",
        "is_free",
    )
    list_editable = (
        "title",
        "author",
        "file",
        "is_free",
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
    readonly_fields = ["duration"]


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
        "is_free",
    )
    list_editable = (
        "title",
        "author",
        "description",
        "file",
        "chapter",
        "is_free",
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
    readonly_fields = ["duration"]


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
        "is_free",
    )
    list_editable = (
        "title",
        "tags",
        "category",
        "file",
        "is_free",
    )
    list_filter = (
        "title",
        "category",
        "pub_date",
        "tags",
    )
    ordering = ("-pub_date",)
    search_fields = ("title",)
    readonly_fields = ["duration"]
