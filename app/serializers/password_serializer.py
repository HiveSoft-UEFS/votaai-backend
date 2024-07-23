from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8) 