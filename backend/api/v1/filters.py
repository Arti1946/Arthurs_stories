from django_filters import rest_framework as filters

from content.models import ContentInfo


class MainPageFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="contains", field_name="title")

    def get_queryset(self):
        return self.queryset.exclude(label="news")

    class Meta:
        fields = ("title",)
        model = ContentInfo
