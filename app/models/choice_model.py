from django.db import models
from .vote_model import Vote
from .option_model import Option


class Choice(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
