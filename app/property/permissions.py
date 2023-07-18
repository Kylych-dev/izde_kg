#Базовый класс пользовательского разрешения
from rest_framework import permissions


class IsPropertyOwner(permissions.BasePermission):
    """
    Класс уровня доступа, то есть в функции 
    где будет стоять этот класс может изменять,
    добавлять в бд данные только владелец этого объяления 
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user