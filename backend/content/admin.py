from django.contrib import admin

from content.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_type",
        "title",
        "author",
        "description",
        "category",
        "chapter",
        "tags",
        "pub_date",
        "file",
        "duration",
        "is_free",
    )
    list_editable = (
        "content_type",
        "title",
        "author",
        "description",
        "category",
        "chapter",
        "tags",
        "file",
        "is_free",
    )
    list_filter = (
        "content_type",
        "tags",
        "title",
        "author",
        "category",
        "pub_date",
    )
    search_fields = (
        "title",
        "author",
    )
    ordering = ("-pub_date",)
    readonly_fields = ["duration"]
