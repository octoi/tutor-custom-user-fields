from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .api import CustomUserViewSet

router = DefaultRouter()
router.register(r'custom-user', CustomUserViewSet, basename='custom-user')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]