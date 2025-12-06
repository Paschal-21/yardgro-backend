from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'role', 'phone_number']
        read_only_fields = ['id']