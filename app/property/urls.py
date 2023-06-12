from rest_framework.routers import DefaultRouter
from .views import PropertyReadView

routers = DefaultRouter()

routers.register('', PropertyReadView, basename='allproperty')


urlpatterns = [
    
] + routers.urls
