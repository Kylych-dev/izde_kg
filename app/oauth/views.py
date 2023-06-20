from rest_framework import generics, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
    AgentSerializer,
    AgentInfoSerializer,
    AgentListSerializer
)
from app.property.models import Advertisement
from app.property.serializers import AdvertisementSerializer

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


class AgentInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Класс для отображении информации об агенте
    """
    serializer_class = AgentInfoSerializer
    queryset = User.objects.filter(is_agent=True)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AgentListSerializer
        return AgentInfoSerializer
    # permission_classes = [IsAgentOrAdminOrReadOnly]


class AddWishlistView(generics.GenericAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        advertisement = self.get_object()
        in_wish_list = Advertisement.objects.filter(wishlist__id=request.user.id,
                                                    pk=advertisement.id).exists()
        if in_wish_list:
            advertisement.wishlist.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT,
                            data={"message": "Deleted from your wishlist"})
        advertisement.wishlist.add(request.user)
        return Response(status=status.HTTP_200_OK, data={"message": "Added to your wishlist"})


class AdsInUserWishListView(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Advertisement.objects.filter(wishlist=self.request.user).order_by('-created_date')
