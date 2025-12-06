from rest_framework import serializers
from ..models import Product, ProductImage 
from ..serializers import ProductImageSerializer

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'uploaded_at']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many = True, read_only=True)
    farmer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 
            'title', 
            'description', 
            'price',
            'quantity',
            'category',
            'farmer',
            'images',
            'created_at'
        ]
class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(Child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'quantity',
            'category',
            'images'
        ]

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)

        for img in images:
            ProductImage.objects.create(product=product, image=img)

        return product