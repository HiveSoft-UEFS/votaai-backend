from django.db import models
from .question_field_model import QuestionField


class Option(models.Model):
    text = models.CharField(max_length=255)
    img = models.BinaryField()
    question = models.ForeignKey(QuestionField, on_delete=models.CASCADE)