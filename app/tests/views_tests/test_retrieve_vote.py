# app/tests/views_tests/test_retrieve_vote.py

from django.test import TestCase
from rest_framework.test import APIClient
from app.models import User  # Certifique-se de que este é o caminho correto para o seu modelo User
from rest_framework import status

class VoteRetrieveTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.client.login(username='admin', password='admin')        

        self.valid_hash = 'hash1'
        self.invalid_hash = 'not'
        self.valid_url = f'/votes/{self.valid_hash}/'
        self.invalid_url = f'/votes/{self.invalid_hash}/'

    def test_retrieve_vote_success(self):
        response = self.client.get(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_vote_failure(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
