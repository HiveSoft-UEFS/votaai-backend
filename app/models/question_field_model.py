from django.db import models
from .poll_model import Poll


class QuestionField(models.Model):
    title = models.CharField(max_length=255)
    max_qtd_choices = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    @property
    def options(self):
        return self.option_set.all()
