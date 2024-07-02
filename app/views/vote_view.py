from rest_framework import status, viewsets
from rest_framework.response import Response
from app.db.queries.vote_queries import VoteQueries
from app.services.vote_service import VoteService
from app.serializers.vote_serializer import VoteSerializer


class VoteViewSet(viewsets.ViewSet):

    _service = VoteService()

    # GET
    def retrieve(self, request, pk=None):
        # Validação de parâmetros
        if pk is None:
            return Response({'error': 'ID necessário'}, status=status.HTTP_400_BAD_REQUEST)

        # Recupera o voto
        vote = self._service.get_vote_by_hash(pk)
        print(vote)
        if vote['success']:
            # Serializa os dados do voto
            serializer = VoteSerializer(data=vote['data'])
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': vote['error']}, status=status.HTTP_404_NOT_FOUND)
