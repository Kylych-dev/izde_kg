from rest_framework import serializers

from .models import (Property, FeedBack, Image, Address, District, City, Advertisement)
from app.oauth.serializers import UserSerializer


class PropertyListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения списка объявлений
    Ограниченный набор полей
    """

    class Meta:
        model = Property

        fields = ('id', 'owner', 'slug', 'purpose')  # Укажите только нужные поля
        # Укажите только нужные поля


class FeedBackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения отзывов
    """
    user = serializers.CharField(source='user.email')
    property = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = FeedBack
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    feedback = FeedBackSerializer(many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True,
                                               default=serializers.CurrentUserDefault())

    class Meta:
        model = Property
        fields = '__all__'

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['images'] = ImagesSerializer(
            instance.images.all(), many=True, context=self.context).data
        context['feedback'] = self.fields['feedback'].to_representation(
            instance.feedback.all())
        context['address'] = AddressSerializer(
            instance.address, many=False).data
        context['owner'] = instance.owner.email
        return context


class ImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения картин
    """

    class Meta:
        model = Image
        fields = ['file', ]


class AddressSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения адреса
    """

    class Meta:
        model = Address
        fields = '__all__'

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['city'] = instance.city.title
        context['district'] = instance.district.title
        return context


class DistrictSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения района
    """

    class Meta:
        model = District
        exclude = ['id', ]


class CitySerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения города
    """

    class Meta:
        model = City


class AdvertisementSerializer(serializers.ModelSerializer):
    "Временный сериалязер"

    class Meta:
        model = Advertisement

        fields = (
            'deal_choices',
            'currency_choices',
            'price',
            'additional_info'
        )

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['region'] = instance.property.address.region
        context['city'] = instance.property.address.city.title
        context['district'] = instance.property.address.district.title
        context['by'] = instance.property.owner.full_name
        return context


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('deal_choices',
                  'currency_choices',
                  'price',
                  'additional_info')

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['location'] = AddressSerializer(instance.property.address).data
        context['owner'] = instance.property.owner.full_name
        context['email'] = instance.property.owner.email
        context['phone'] = instance.property.owner.phone

        return context
