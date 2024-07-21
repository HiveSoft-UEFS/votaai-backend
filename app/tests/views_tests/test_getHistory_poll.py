# app/tests/views_tests/test_get_history.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import jwt
from django.conf import settings
from app.models import User  # Certifique-se de que este é o caminho correto para o seu modelo User

class GetHistoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Criar um usuário de teste
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Criar um token JWT para o usuário
        self.token = jwt.encode({'user_id': self.user.id}, settings.SECRET_KEY, algorithm='HS256')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.history_url = '/your-endpoint/history/'  # Atualize com o URL correto

    def test_get_history_success(self):
        response = self.client.get(self.history_url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Adicione mais asserções para verificar o conteúdo da resposta, se necessário

    def test_missing_authorization_header(self):
        response = self.client.get(self.history_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"detail": "Authorization header is missing"})

    def test_invalid_token(self):
        invalid_token = 'invalidtoken'
        headers = {'HTTP_AUTHORIZATION': f'Bearer {invalid_token}'}
        response = self.client.get(self.history_url, **headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {"detail": "Invalid token"})

    def test_expired_token(self):
        expired_token = jwt.encode({'user_id': self.user.id, 'exp': 0}, settings.SECRET_KEY, algorithm='HS256')
        headers = {'HTTP_AUTHORIZATION': f'Bearer {expired_token}'}
        response = self.client.get(self.history_url, **headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {"detail": "Token has expired"})
