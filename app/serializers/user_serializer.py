from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin
from app.models import User

class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']
        extra_kwargs = {
            'email': {'required': False},
            'username': {'required': False},
        }
