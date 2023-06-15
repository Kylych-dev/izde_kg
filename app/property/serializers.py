from rest_framework import serializers
from .models import Property, FeedBack


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
    feedback = FeedBackSerializer(many=True)

    class Meta:
        """

        """
        model = Property
        fields = '__all__'

    def to_representation(self, instance):
        context = super().to_representation(instance)
        feedback_data = self.fields['feedback'].to_representation(
            instance.feedback.all())
        context['feedback'] = feedback_data
        return context
