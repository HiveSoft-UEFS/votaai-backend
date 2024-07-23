import unittest
from unittest.mock import patch, MagicMock
from app.services.vote_service import VoteService
from app.db.queries.vote_queries import VoteQueries

class VoteServiceTests(unittest.TestCase):
    
    def setUp(self):
        self.vote_service = VoteService()
    
    @patch.object(VoteQueries, 'get_all', return_value=[{'id': 1, 'name': 'Test Vote'}])
    def test_get_all_votes_success(self, mock_get_all):
        response = self.vote_service.get_all_votes()
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{'id': 1, 'name': 'Test Vote'}])
        mock_get_all.assert_called_once()
    
    @patch.object(VoteQueries, 'get_all', side_effect=Exception("Database error"))
    def test_get_all_votes_failure(self, mock_get_all):
        response = self.vote_service.get_all_votes()
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], 'Database error')
        mock_get_all.assert_called_once()

    @patch.object(VoteQueries, 'createVote', return_value={'id': 1, 'date': '2024-07-20'})
    def test_create_vote_success(self, mock_create_vote):
        response = self.vote_service.createVote()
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], {'id': 1, 'date': '2024-07-20'})
        mock_create_vote.assert_called_once()

    @patch.object(VoteQueries, 'createVote', side_effect=Exception("Failed to create vote"))
    def test_create_vote_failure(self, mock_create_vote):
        response = self.vote_service.createVote()
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], 'Failed to create vote')
        mock_create_vote.assert_called_once()

if __name__ == '__main__':
    unittest.main()
