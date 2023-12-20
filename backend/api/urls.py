from . import views
from rest_framework import routers


router = routers.DefaultRouter();
router.register('api', views.ApiViewSet, basename='api')

urlpatterns = [
    
]

urlpatterns += router.urls
