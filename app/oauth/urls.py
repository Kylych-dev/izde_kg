from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CustomUserViewSet, CreateTokenView)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('token/', CreateTokenView.as_view(), name='token')] + router.urls

