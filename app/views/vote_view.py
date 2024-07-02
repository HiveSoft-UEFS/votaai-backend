from rest_framework import status, viewsets
from rest_framework.response import Response
from app.db.queries.vote_queries import VoteQueries
from app.services.vote_service import VoteService
from app.serializers.vote_serializer import VoteSerializer


class VoteViewSet(viewsets.ViewSet):

    _service = VoteService()

    # GET
    def list(self, request):
        votes = self._service.get_all_votes()
        if votes['success']:
            return Response(votes['data'], status=status.HTTP_200_OK)
        return Response({'error': votes['error']}, status=status.HTTP_404_NOT_FOUND)

    # GET
    def retrieve(self, request, pk=None):
        # Validação de parâmetros
        if pk is None:
            return Response({'error': 'ID necessário'}, status=status.HTTP_400_BAD_REQUEST)

        # Recupera o voto
        vote = self._service.get_vote_by_hash(pk)
        print(vote['data'])
        if vote['success']:
            return Response(vote['data'], status=status.HTTP_200_OK)
        return Response({'error': vote['error']}, status=status.HTTP_404_NOT_FOUND)