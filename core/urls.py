from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("home.urls")),
    path("icons/", include("icons.urls")),
    path("categories/", include("categories.urls")),
    path("products/", include("products.urls")),
]
