from django.shortcuts import render
from app.db.queriesUser import insert_user

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializer import UserSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.validated_data
        insert_user(new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)