from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.services.poll_service import PollService
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import jwt
from django.conf import settings




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
        if pk is None:
            return Response({'error': 'ID necessário'}, status=status.HTTP_400_BAD_REQUEST)
    
        poll = self._service.get_poll_by_id(pk)
        if poll['success']:
            return Response(poll['data'], status=status.HTTP_200_OK)
        return Response({'error': poll['error']}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], url_path='participation', permission_classes=[IsAuthenticated])
    def get_participation(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if not authorization_header:
            return Response({"detail": "Authorization header is missing"}, status=400)

        token = authorization_header.split()[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return Response({"detail": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return Response({"detail": "Invalid token"}, status=401)

        poll_counts = self._service.get_poll_counts_by_user(user_id)

        if poll_counts['success']:
            return Response(poll_counts['data'], status=status.HTTP_200_OK)

        return Response({'error': poll_counts['error']}, status=status.HTTP_404_NOT_FOUND)
    
    
    def search(self, request):
        order = request.GET.get('order')
        category = request.GET.get('category')
        value = request.GET.get('value')
        if value is None: value = ''
        if order == '' or order is None: order = 'new'
        if category == '' or category is None: category = 'all'
        if request.GET.get('tag') == 'true':
            poll = self._service.get_poll_by_tag(order, category, value)
        elif request.GET.get('code') == 'true':
            poll = self._service.get_poll_by_code(value)
        else:
            poll = self._service.get_poll_by_title(order, category, value)
        if poll['success']:
            return Response(poll['data'], status=status.HTTP_200_OK)
        return Response({'error': poll['error']}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], url_path='history', permission_classes=[IsAuthenticated])
    def get_history(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if not authorization_header:
            return Response({"detail": "Authorization header is missing"}, status=400)

        token = authorization_header.split()[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return Response({"detail": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return Response({"detail": "Invalid token"}, status=401)

        poll_service = PollService()
        poll_history = poll_service.get_history_by_id(user_id)

        if not poll_history['success']:
            return Response({"detail": poll_history['error']['message']}, status=500)

        return Response(poll_history['data'])
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
