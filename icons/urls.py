from django.urls import path, include
from rest_framework import routers

from icons import viewsets

router = routers.SimpleRouter()

router.register(r"icons", viewsets.IconViewSet, basename="icon")


urlpatterns = [
    path("", include(router.urls))
]