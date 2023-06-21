from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserAPIView,
                    CreateTokenView,
                    AgentAPIView,
                    AddWishlistView,
                    AdsInUserWishListView,
<<<<<<< HEAD
                    AdsInUserWishListDetailView)
=======
                    AgentInfoViewSet)
>>>>>>> 371cd79ccc901e03daee60a319794b058f75582e

router = DefaultRouter()
# router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'agents', AgentInfoViewSet, basename='agents')

urlpatterns = [
    path('register/', UserAPIView.as_view(), name='create-user'),
    path('become-agent/', AgentAPIView.as_view(), name='create-agent'),
    path('login/', CreateTokenView.as_view(), name='token'),
    path('add-wishlist/<int:pk>/', AddWishlistView.as_view(), name='add-wishlist'),
    path('wishlist/', AdsInUserWishListView.as_view(), name='user-wishlist'),
    path('ads-details/', AdsInUserWishListDetailView.as_view(), name='ads-detail')


]
urlpatterns += router.urls
