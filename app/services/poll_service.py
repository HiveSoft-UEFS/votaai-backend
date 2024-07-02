from app.db.queries.poll_queries import PollQueries


class PollService:

    def get_all_polls(self):
        try:
            votes = PollQueries.get_all()
            return {"success": True, "data": votes}
        except Exception as e:
            return {"success": False, "error": str(e)}
