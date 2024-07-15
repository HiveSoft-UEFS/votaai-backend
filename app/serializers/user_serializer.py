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

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        # Aqui você pode adicionar outras validações, como complexidade da senha
        return attrs