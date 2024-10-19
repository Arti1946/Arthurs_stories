from rest_framework import permissions
from rest_framework.permissions import BasePermission


class FavoritePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if (
            user.is_authenticated
            and (
                view.action == "favorite"
                and request.method in ["POST", "DELETE"]
            )
            or request.method in permissions.SAFE_METHODS
        ):
            return True
        return False
