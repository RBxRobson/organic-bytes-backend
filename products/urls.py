from django.urls import path, include
from rest_framework import routers
from products import viewsets

router = routers.SimpleRouter()
router.register(r"", viewsets.ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls))
]
