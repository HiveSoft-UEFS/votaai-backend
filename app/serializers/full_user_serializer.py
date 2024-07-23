from rest_framework import serializers
from app.models import User

class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Inclui todos os campos do modelo User
