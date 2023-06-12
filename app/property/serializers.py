from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения всех объявлений
    """
    class Meta:
        model = Property
        fields = '__all__'


