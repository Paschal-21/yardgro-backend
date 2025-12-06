from rest_framework import viewsets, permissions
from inventory.models import Product
from inventory.serializers.product_serializers import (
    ProductSerializer,
    ProductCreateSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        # Use different serializers for create/update vs read
        if self.action in ["create", "update", "partial_update"]:
            return ProductCreateSerializer
        return ProductSerializer

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)