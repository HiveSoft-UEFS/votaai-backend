import unittest
from unittest.mock import patch
from app.services.poll_service import PollService
from app.db.queries.poll_queries import PollQueries



class pollServiceTests(unittest.TestCase):

    def setUp(self):
        self.pollService = PollService()

    @patch.object(PollQueries, 'get_all', return_value=[{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
    def test_all_polls_sucess(self, mock_get_all):
        response = self.pollService.get_all_polls()
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
        mock_get_all.assert_called_once()

    @patch.object(PollQueries, 'get_all', side_effect=Exception("Database error"))
    def test_all_polls_fail(self,mock_get_all):
        response = self.pollService.get_all_polls()
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], 'Database error' )
        mock_get_all.assert_called_once()


    @patch.object(PollQueries, 'get_by_id', return_value={"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"})
    def test_get_poll_id_sucess(self, mock_get_id):
        response = self.pollService.get_poll_by_id(1)
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], {"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"})
        mock_get_id.assert_called_once()


    @patch.object(PollQueries, 'get_by_id', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_poll_id_fail(self, mock_get_id):
        response = self.pollService.get_poll_by_id(0)
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_id.assert_called_once()


    @patch.object(PollQueries, 'get_where', return_value=[{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
    def test_get_poll_by_title_sucess(self, mock_get_title):
        response = self.pollService.get_poll_by_title('old','TEST','TEST')
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
        mock_get_title.assert_called_once()

    
    
    @patch.object(PollQueries, 'get_where', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_poll_by_title_fail(self, mock_get_title):
        response = self.pollService.get_poll_by_title('old','TEST','TEST')
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_title.assert_called_once()



    @patch.object(PollQueries, 'get_where', return_value=[{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
    def test_get_poll_by_tag_sucess(self, mock_get_tag):
        response = self.pollService.get_poll_by_tag('old','TEST','TEST')
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
        mock_get_tag.assert_called_once()

    @patch.object(PollQueries, 'get_where', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_poll_by_tag_fail(self, mock_get_tag):
        response = self.pollService.get_poll_by_tag('old','TEST','TEST')
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_tag.assert_called_once()



    @patch.object(PollQueries, 'get_where', return_value=[{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
    def test_get_poll_by_code_sucess(self, mock_get_code):
        response = self.pollService.get_poll_by_code('')
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
        mock_get_code.assert_called_once()


    @patch.object(PollQueries, 'get_where', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_poll_by_code_fail(self, mock_get_code):
        response = self.pollService.get_poll_by_code('')
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_code.assert_called_once()


    @patch.object(PollQueries, 'get_user_polls', return_value=[{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
    def test_get_hist_id_sucess(self, mock_get_hist):
        response = self.pollService.get_history_by_id(1)
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], [{"id": 1,"criation_date": "2012-07-30","finish_date": "1976-09-05","status": "OPEN","title": "Blue concern me.","description": "Ball response around star stock.","privacy": "PUBLIC","creator_id": 8,"category": "art","code": None,"tags": "#onepiece"}])
        mock_get_hist.assert_called_once()


    @patch.object(PollQueries, 'get_user_polls', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_hist_id_fail(self, mock_get_hist):
        response = self.pollService.get_history_by_id(1)
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_hist.assert_called_once()

    @patch.object(PollQueries, 'get_poll_counts_by_user', return_value={'criadas': 2, 'participadas': 45})
    def test_get_cont_id_sucess(self, mock_get_part):
        response = self.pollService.get_poll_counts_by_user(1)
        self.assertTrue(response['success'])
        self.assertEqual(response['data'], {'criadas': 2, 'participadas': 45})
        mock_get_part.assert_called_once()


    @patch.object(PollQueries, 'get_poll_counts_by_user', side_effect=Exception("psycopg2.OperationalError"))
    def test_get_cont_id_fail(self, mock_get_part):
        response = self.pollService.get_poll_counts_by_user(1)
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "psycopg2.OperationalError")
        mock_get_part.assert_called_once()


    


   







if __name__ == '__main__':
    unittest.main()




