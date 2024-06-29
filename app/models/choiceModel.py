from django.db import models
from .voteModel import Vote
from .optionModel import Option

class Choice(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)