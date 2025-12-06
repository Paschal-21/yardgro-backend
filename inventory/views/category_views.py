from rest_framework import viewsets, permissions
from inventory.models import Category
from inventory.serializers.category_serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]