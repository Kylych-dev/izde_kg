from rest_framework import serializers
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (get_user_model,
                                 authenticate, )
from .models import Language
from app.realtor.models import Agent


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    "Сериаляйзер для регистрации пользователя, который ничего не публикует"

    languages = LanguageSerializer(many=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['photo',
                  'full_name',
                  'languages',
                  'email',
                  'phone',
                  'is_agent',
                  'password',
                  'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        language_data = validated_data.pop('languages')
        user = get_user_model().objects.create_user(**validated_data)
        for language in language_data:
            language, created = Language.objects.get_or_create(title=language['title'])
            user.languages.add(language)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

    def validated_full_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(_("Name is too short"))
        else:
            return value

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if not password == confirm_password:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the User auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the User."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['User'] = user
        return attrs


class AgentViewSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения информации об агенте
    """
    class Meta:
        model = Agent
        fields = '__all__'
        
    def to_representation(self, instance):
        return super().to_representation(instance)
        

class FeedbackAgent(serializers.ModelSerializer):
    """
    Сериалайзер для отображения отзывов об агенте
    """
    pass