
import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from app.models import User  # Ajuste o caminho conforme sua estrutura de projeto
from rest_framework_simplejwt.tokens import RefreshToken

class PollTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create_user(username='d2d2', password='d2d2',cpf='d2d2',email='afafa',name='', lname='',status= '', role= '')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.polls_url = '/votes/'
        self.poll_detail_url = lambda pk: f'/polls/{pk}/'
        self.participation_url = '/polls/participation/'
        self.history_url = '/polls/history/'
        self.create_poll_url= '/polls/'




    def test_list_polls(self):
        data = {'test': {'1': [1]}}
        response = self.client.post(
            self.polls_url,
            data=json.dumps(data),  # Serializa os dados para JSON
            content_type='application/json'  # Define o tipo de conteúdo como JSON
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)