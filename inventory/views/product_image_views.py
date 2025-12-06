from rest_framework import viewsets, permissions
from inventory.models import ProductImage
from inventory.serializers.product_serializers import ProductImageSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.request.data.get("product")
        serializer.save(product_id=product_id)