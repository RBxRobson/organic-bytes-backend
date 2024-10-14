from django.urls import path, include
from rest_framework import routers

from categories import viewsets

router = routers.SimpleRouter()

router.register(r"categories", viewsets.CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls))
]