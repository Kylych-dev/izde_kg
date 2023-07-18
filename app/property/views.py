from .serializers import PropertySerializer, PropertyListSerializer
from .permissions import IsPropertyOwner
from .models import Property

from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render
from django.contrib.auth import get_user_model


class PropertyViewSet(viewsets.ModelViewSet):
    """
    Класс отображения для объявлений
    Пользователи могут читать, искать и фильтровать объявления
    Авторы и владельцы могут выполнять CRUD-действия
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['storey', 'bedroom', 'bathroom',
                     'furnished', 'parking_space',
                     'new_property', 'purpose', 'duration',
                     'square_meter', 'address__region',
                     'address__city__title', 'address__district__title']

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        return PropertySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Назначить текущего пользователя в качестве владельца объявления
            user = self.request.user
            serializer.save(owner=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         permission_classes = [IsPropertyOwner]
    #     else:
    #         permission_classes = [IsAuthenticated]

    #     return [permission() for permission in permission_classes]
