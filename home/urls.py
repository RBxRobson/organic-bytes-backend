from django.urls import path, include
from rest_framework import routers

from home import viewsets

router = routers.SimpleRouter()

router.register(r"hero/banners", viewsets.HeroViewSet, basename="banners")


urlpatterns = [
    path("", include(router.urls))
]