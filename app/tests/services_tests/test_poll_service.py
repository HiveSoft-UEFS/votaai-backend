import unittest
from unittest.mock import patch
from app.db.queries.poll_queries import PollQueries
from app.services.poll_service import PollService
















class pollServiceTests(unittest.TestCase):

    def setUp(self):
        self.pollService = PollService()

    @patch.object(PollQueries, 'get_all', return_value=[{'id': 1, 'name': 'Test Vote'}])
    def test_all_polls_sucess(self, mock_get_all):
        pass


    pass
