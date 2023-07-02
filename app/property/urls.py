from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

routers = DefaultRouter()

routers.register('', PropertyViewSet, basename='allproperty')


urlpatterns = [
    
] + routers.urls
