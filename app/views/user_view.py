from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ViewSet):

    # GET
    def list(self, request):
        # Aqui você pode implementar a lógica para lidar com solicitações GET
        return Response({'message': 'Hello, world!'})

    # GEt
    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    # POST
    def create(self, request):
        # Aqui você pode implementar a lógica para lidar com solicitações POST
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.validated_data
            queries_user.insert_user(new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def update(self, request, pk=None):
        return Response({'method': f'PUT for {type(request.data)}'})

    # PATCH
    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    # DELETE
    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})