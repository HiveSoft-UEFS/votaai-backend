from app.db.queries.vote_queries import VoteQueries
from datetime import datetime


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
        

    def createChoices(self,options,vote_id):
        choices = []
        try:
            for i in options:
                #print(i, 'For')
                choice = VoteQueries.createChoice(i,vote_id)
                choices.append(choice)
            return {"success": True, "data": choices}
        except Exception as e:
            '''print(vote_id, type(vote_id))
            print(choices)
            print(e)'''
            return {"success": False, "error": str(e)}
        

    def createVote(self):
        date = datetime.now()
        try:
            vote = VoteQueries.createVote(date)
            return {"success": True, "data": vote}
        except Exception as e:
            return {"success": False, "error": str(e)}
        

    def updateHash(self,hash,idVote):
        try:
            vote = VoteQueries.updateVoteHash(hash,idVote)
            return {"success": True, "data": vote}
        except Exception as e:
            return {"success": False, "error": str(e)}
        

    def getLastVote(self):
        try:
            vote = VoteQueries.getLastVote()
            return {"success": True, "data": vote}
        except Exception as e:
            return {"success": False, "error": str(e)}
        

    def participation(self,user, poll):
        try:
            participation = VoteQueries.createParticipation(user,poll)
            return {"success": True, "data": participation}
        except Exception as e:
            return {"success": False, "error": str(e)}

        

