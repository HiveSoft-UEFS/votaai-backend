from app.db.queries.poll_queries import PollQueries


class PollService:

    def get_all_polls(self):
        try:
            votes = PollQueries.get_all()
            return {"success": True, "data": votes}
        except Exception as e:
            return {"success": False, "error": str(e)}
        

    def get_Poll_By_Id(self,id):

        try:
            poll = PollQueries.get_by_id(id)
            return {"success": True, "data": poll}
        
        except Exception as e:
            return {"success": False, "error": str(e)}
