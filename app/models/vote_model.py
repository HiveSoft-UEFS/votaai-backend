from django.db import models


class Vote(models.Model):
    hash = models.CharField(max_length=255)
    date = models.DateField()