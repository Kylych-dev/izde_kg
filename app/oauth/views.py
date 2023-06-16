from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    AuthTokenSerializer, AgentSerializer)

User = get_user_model()


class UserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class AgentAPIView(generics.UpdateAPIView):
    serializer_class = AgentSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return User.objects.get(pk=self.request.user.id, is_agent=False)


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['User']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# class AgentInfoView(viewsets.ModelViewSet):
#     """
#     Класс для отображении информации об агенте
#     """
#     serializer_class = AgentViewSerializer
#     queryset = Agent.objects.all()
#     permission_classes = [IsAgentOrAdminOrReadOnly]
