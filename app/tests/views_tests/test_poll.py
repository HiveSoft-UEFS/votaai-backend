
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
        self.polls_url = '/polls/'
        self.poll_detail_url = lambda pk: f'/polls/{pk}/'
        self.participation_url = '/polls/participation/'
        self.history_url = '/polls/history/'
        self.create_poll_url= '/polls/'




    def test_list_polls(self):
        response = self.client.get(self.polls_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_poll(self):
        response = self.client.get(self.poll_detail_url(1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_poll_not_found(self):
        response = self.client.get(self.poll_detail_url(999)) 
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_polls(self):
        response = self.client.get('/polls/search/s', {'order': 'new', 'category': 'all', 'value': 'example'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_participation_success(self):
        response = self.client.get(self.participation_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_history_success(self):
        response = self.client.get(self.history_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_poll_success(self):
        data = {"id": 999,
                "criation_date": "2012-07-30",
                "finish_date": "1976-09-05",
                "status": "OPEN",
                "title": "Blue concern me.",
                "description": "Ball response around star stock.",
                "privacy": "PUBLIC",
                "creator_id": 8,
                "category": "art",
                "code": None,
                "tags": "#onepiece"}
        response = self.client.post(self.create_poll_url, data, format='json')
        print("Response Data:", response.data)  # Para depuração
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_poll_failure(self):
        data = {"id": 999,
                "criation_date": "2012-07-30",
                "finish_date": "1976-09-05",
                "status": "OPEN",
                "title": "Blue concern me.",
                "description": "Ball response around star stock.",
                "privacy": "PUBLIC",
                "creator_id": 8,
                "category": "art",
                "code": None,
                "tags": "#onepiece"}
        response = self.client.post(self.create_poll_url, data, format='json')
        print("Response Data:", response.data)  # Para depuração
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)





