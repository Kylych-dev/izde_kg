from .serializers import PropertySerializer
from .permissions import IsPropertyOwner
from .models import Property

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render



class PropertyViewSet(viewsets.ModelViewSet):
    """
    Класс отображения для объявлений
    Пользователи могут читать, искать и фильтровать объchangesявления
    Авторы и владельцы могут выполнять CRUD-действия
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
<<<<<<< HEAD

    @action(detail=False, methods=['get'])
    def search(self, request, **kwargs):
        """
        Функция поиска, через endpoints
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Применение фильтров
        storey = request.query_params.get('storey')
        if storey:
            queryset = queryset.filter(storey=storey)

        bedroom = request.query_params.get('bedroom')
        if bedroom:
            queryset = queryset.filter(bedroom=bedroom)

        bathroom = request.query_params.get('bathroom')
        if bathroom:
            queryset = queryset.filter(bathroom=bathroom)

        furnished = request.query_params.get('furnished')
        if furnished:
            queryset = queryset.filter(furnished=furnished)

        parking_space = request.query_params.get('parking_space')
        if parking_space:
            queryset = queryset.filter(parking_space=parking_space)

        new_property = request.query_params.get('new_property')
        if new_property:
            queryset = queryset.filter(new_property=new_property)

        purpose = request.query_params.get('purpose')
        if purpose:
            queryset = queryset.filter(purpose=purpose)

        duration = request.query_params.get('duration')
        if duration:
            queryset = queryset.filter(duration=duration)

        square_meter_min = request.query_params.get('square_meter_min')
        square_meter_max = request.query_params.get('square_meter_max')
        if square_meter_min and square_meter_max:
            queryset = queryset.filter(square_meter__range=(square_meter_min, square_meter_max))

        region = request.query_params.get('region')
        if region:
            queryset = queryset.filter(address__region=region)
=======
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['storey', 'bedroom', 'bathroom', 
                     'furnished', 'parking_space', 
                     'new_property', 'purpose', 'duration', 
                     'square_meter', 'address__region', 
                     'address__city__title', 'address__district__title']

    # @action(detail=False, methods=['get'])
    # def search(self, request, **kwargs):
    #     """
    #     Функция поиска, через endpoints
    #     """
    #     queryset = self.filter_queryset(self.get_queryset())

    #     # Применение фильтров
    #     storey = request.query_params.get('storey')
    #     if storey:
    #         queryset = queryset.filter(storey=storey)

    #     bedroom = request.query_params.get('bedroom')
    #     if bedroom:
    #         queryset = queryset.filter(bedroom=bedroom)

    #     bathroom = request.query_params.get('bathroom')
    #     if bathroom:
    #         queryset = queryset.filter(bathroom=bathroom)

    #     furnished = request.query_params.get('furnished')
    #     if furnished:
    #         queryset = queryset.filter(furnished=furnished)

    #     parking_space = request.query_params.get('parking_space')
    #     if parking_space:
    #         queryset = queryset.filter(parking_space=parking_space)

    #     new_property = request.query_params.get('new_property')
    #     if new_property:
    #         queryset = queryset.filter(new_property=new_property)

    #     purpose = request.query_params.get('purpose')
    #     if purpose:
    #         queryset = queryset.filter(purpose=purpose)

    #     duration = request.query_params.get('duration')
    #     if duration:
    #         queryset = queryset.filter(duration=duration)

    #     square_meter_min = request.query_params.get('square_meter_min')
    #     square_meter_max = request.query_params.get('square_meter_max')
    #     if square_meter_min and square_meter_max:
    #         queryset = queryset.filter(square_meter__range=(square_meter_min, square_meter_max))

    #     region = request.query_params.get('region')
    #     if region:
            
    #         queryset = queryset.filter(address__region=region)
>>>>>>> 86c92ffcffcec10002b5c305fd50665018884bd8

    #     city = request.query_params.get('city')
    #     if city:
    #         queryset = queryset.filter(address__city__title=city)

    #     district = request.query_params.get('district')
    #     if district:
    #         queryset = queryset.filter(address__district__title=district)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsPropertyOwner]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
