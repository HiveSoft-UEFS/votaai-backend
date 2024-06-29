from django.db import models
from .pollModel import Poll

class QuestionField(models.Model):
    title = models.CharField(max_length=255)
    max_qtd_choices = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)