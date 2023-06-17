from rest_framework import serializers
from .models import Property, FeedBack, Image, Advertisement


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
    """
    Сериализатор для отображения всех объявлений
    """

    class Meta:
        model = Property
        fields = '__all__'

    feedback = FeedBackSerializer(many=True)

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['images'] = ImagesSerializer(
            instance.images.all(), many=True, context=self.context).data
        feedback_data = self.fields['feedback'].to_representation(
            instance.feedback.all())
        context['feedback'] = feedback_data
        return context


class ImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения картин
    """

    class Meta:
        model = Image
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
