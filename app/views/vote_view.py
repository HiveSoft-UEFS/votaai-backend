import json
import hashlib
import jwt


from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.response import Response
from app.db.queries.vote_queries import VoteQueries
from app.services.vote_service import VoteService
from app.serializers.vote_serializer import VoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class VoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    _service = VoteService()

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

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
      
        if vote['success']:
            return Response(vote['data'], status=status.HTTP_200_OK)
        return Response({'error': vote['error']}, status=status.HTTP_404_NOT_FOUND)
    
    # POST
    def create(self, request):
        
        if request.method == 'POST':
            authorization_header = request.META['HTTP_AUTHORIZATION']
            token = authorization_header.split()[1] if authorization_header else None
                        
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']


            data = json.loads(request.body)
            print(data)
            lastvote = self._service.getLastVote()
            vote = self._service.createVote()
            if lastvote['success']:
                lastvote = lastvote['data']

            if vote['success']:
                vote = vote['data']

           
            options = []
            for i in data:
                pollId = i
                for j in data[i]:
                    for y in data[i][j]:
                        options.append(y)
            choices = self._service.createChoices(options, vote['id'])


            hash_obj = hashlib.md5()

            if lastvote:
                ultima_hash = lastvote['hash']
                obj = {"ultima_hash":ultima_hash, "choices" : choices}
                obj_json = json.dumps(obj, sort_keys=True)
                hash_obj.update(obj_json.encode())
                hash_hex = hash_obj.hexdigest()

            else:
                obj = {"ultima_hash":None, "choices" : choices}
                obj_json = json.dumps(obj, sort_keys=True)
                hash_obj.update(obj_json.encode())
                hash_hex = hash_obj.hexdigest()

            vote = self._service.updateHash(hash_hex,vote['id'])


            participation = self._service.participation(user_id,pollId)
            print(participation)


                



        return Response (vote)
