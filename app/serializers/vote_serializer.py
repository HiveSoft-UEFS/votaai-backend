from rest_framework import serializers
from app.models import User, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['hash']
