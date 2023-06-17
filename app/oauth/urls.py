from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserAPIView, CreateTokenView, AgentAPIView)

# router = DefaultRouter()
# router.register(r'users', CustomUserViewSet, basename='user')
# # router.register(r'agents', AgentInfoView, basename='agents')

urlpatterns = [
    path('create/', UserAPIView.as_view(), name='create-user'),
    path('update/', AgentAPIView.as_view(), name='create-agent'),
    path('token/', CreateTokenView.as_view(), name='token'),
    ]
