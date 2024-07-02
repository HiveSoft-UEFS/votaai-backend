from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.services.poll_service import PollService


class PollViewSet(viewsets.ViewSet):

    _service = PollService()

    # GET
    def list(self, request):
        polls = self._service.get_all_polls()
        if polls['success']:
            return Response(polls['data'], status=status.HTTP_200_OK)
        return Response({'error': polls['error']}, status=status.HTTP_404_NOT_FOUND)

    # GEt
    def retrieve(self, request, pk=None):
        pass

    # POST
    def create(self, request):
        pass

    # PUT
    def update(self, request, pk=None):
        pass

    # PATCH
    def partial_update(self, request, pk=None):
        return Response({'error': 'Not Implemented'})

    # DELETE
    def destroy(self, request, pk=None):
        pass