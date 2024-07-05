from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model  
from rest_framework import serializers

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise serializers.ValidationError('No user found with provided credentials.')

            if user.password == password:  # Use check_password para verificar a senha
                token = self.get_token(user)
                return {
                    'access': str(token.access_token),
                }
            else:
                raise serializers.ValidationError('Incorrect password.')
        
        raise serializers.ValidationError('Must include both "username" and "password"')