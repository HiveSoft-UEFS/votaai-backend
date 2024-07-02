from app.db.queries.vote_queries import VoteQueries


class VoteService:

    def get_all_votes(self):
        try:
            votes = VoteQueries.get_all()
            return {"success": True, "data": votes}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_vote_by_hash(self, hash):
        try:
            votes = VoteQueries.getVote(hash)
            return {"success": True, "data": votes}
        except Exception as e:
            return {"success": False, "error": str(e)}
