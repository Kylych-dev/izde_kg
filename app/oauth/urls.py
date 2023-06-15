from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CustomUserViewSet, CreateTokenView, AgentInfoView)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'agents', AgentInfoView, basename='agents')

urlpatterns = [
    path('token/', CreateTokenView.as_view(), name='token')] + router.urls
