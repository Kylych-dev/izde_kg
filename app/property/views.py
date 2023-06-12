from django.shortcuts import render
from requests import request
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PropertyReadView(viewsets.ReadOnlyModelViewSet):
    """
    Класс для отображений всех объявлений, только для чтения
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    

class PropertyView(viewsets.ModelViewSet):
    """
    Класс для добавления, редактирования и удаления объявления, работает только для владельца
    """
    queryset = Property.objects.all()  #filter(owner = request.user)
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @action(detail=False, methods=['get'])
    def search(self, request, **kwargs):
        property = self.get_queryset()
        kwarg = {}
        category = request.query_params.get('category')
        if category:
            kwargs['category_id'] = category
        property = property.filter
        