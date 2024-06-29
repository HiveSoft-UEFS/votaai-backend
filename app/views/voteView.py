from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.db.queriesVote import getVote

class VoteDetailView(APIView):
    def get(self, request, hash, format=None):
        vote = getVote(hash)
        if vote is not None:
            return Response(vote, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Vote not found'}, status=status.HTTP_404_NOT_FOUND)
