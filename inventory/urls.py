from rest_framework.routers import DefaultRouter
from django.urls import path, include

from inventory.views.product_views import ProductViewSet
from inventory.views.category_views import CategoryViewSet
from inventory.views.product_image_views import ProductImageViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("categories", CategoryViewSet, basename="categories")
router.register("product-images", ProductImageViewSet, basename="product-images")

urlpatterns = [
    path("", include(router.urls)),
]