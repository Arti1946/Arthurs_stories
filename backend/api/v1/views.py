from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.v1.serializers import ContentSerializer
from content.models import Content


@extend_schema(tags=["Контент"])
@extend_schema_view(
    list=extend_schema(
        summary="Список контента",
    ),
    retrieve=extend_schema(summary="Контент"),
)
class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options"]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return Content.objects.all()
        return Content.objects.filter(is_free=True)

    @extend_schema(
        summary="Тип контента",
        description="Получение списка контента определенного типа",
    )
    @action(
        detail=False, methods=["get"], url_path=r"(?P<content_type>[a-zA-Z]+)"
    )
    def content_type(self, request, content_type):
        content = Content.objects.filter(content_type=content_type)
        serializer = ContentSerializer(content, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
