from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Category

class CategorySerializer(serializers.Modelserializer):
    class Meta:
        model = Category 
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']
