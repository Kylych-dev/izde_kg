from rest_framework import permissions


class IsAgentOrAdminOrReadOnly(permissions.BasePermission):
    """
    Класс для определения текущего пользователя агент или другой пользователь 
    """

    def has_permission(self, request, view):
        # Разрешить чтение для всех пользователей
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить CRUD-действия только агентам и администраторам
        return request.user.is_authenticated and (request.user.is_agent or request.user.is_staff)
