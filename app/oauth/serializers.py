from rest_framework import serializers
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (get_user_model,
                                 authenticate, )
from .models import (Language, Region, Feedback, CustomUser)

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
        instance.full_name = validated_data.get(
            'full_name', instance.full_name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.experience = validated_data.get(
            'experience', instance.experience)
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


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class AgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'photo', 'description')


class AgentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('description',)

    def get_photo(self, instance):
        if instance.photo:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(instance.photo.url)
        return None

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and request.query_params.get('detail'):
            return super().to_representation(instance)
        else:
            return {
                'full_name': instance.full_name,
                'photo': self.get_photo(instance),
                'email': instance.email,
                'phone': str(instance.phone),
                'feedback': self.get_feedbacks_received(instance),
            }

    def get_feedbacks_received(self, instance):
        feedbacks = instance.feedbacks_received.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return serializer.data


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


class FeedbackAgent(serializers.ModelSerializer):
    """
    Сериалайзер для отображения отзывов об агенте
    """
    #    model = User
    #    fields = ['']
    # pass
