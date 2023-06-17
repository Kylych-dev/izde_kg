from rest_framework import serializers
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (get_user_model,
                                 authenticate, )
from .models import (Language, Region)

User = get_user_model()


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['title']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email',
                  'password',
                  'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if not password == confirm_password:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs


class AgentSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=True, required=True)
    languages = LanguageSerializer(many=True, required=True)
    full_name = serializers.CharField(required=True)
    phone = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['photo',
                  'full_name',
                  'description',
                  'phone',
                  'languages',
                  'experience',
                  'region',
                  'is_agent',
                  ]

    def validated_full_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(_("Name is too short"))
        else:
            return value

    def update(self, instance, validated_data):
        regions_data = validated_data.pop('region')
        languages_data = validated_data.pop('languages')
        instance.photo = validated_data.get('photo', instance.photo)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.description = validated_data.get('description', instance.description)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.is_agent = True
        instance.save()

        for language_data in languages_data:
            title = language_data['title'].capitalize()
            language, _ = Language.objects.get_or_create(title=title)
            instance.languages.add(language)

        for region_data in regions_data:
            title = region_data['title'].capitalize()
            region, _ = Region.objects.get_or_create(title=title)
            instance.region.add(region)

        return instance


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


class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
    def to_representation(self, instance):
        return super().to_representation(instance)
        

class FeedbackAgent(serializers.ModelSerializer):
    """
    Сериалайзер для отображения отзывов об агенте
    """
    pass

