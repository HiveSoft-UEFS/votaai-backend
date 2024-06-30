from django.db import models
from .user_model import User


class Poll(models.Model):
    criation_date = models.DateField()
    finish_date = models.DateField()
    status = models.CharField(max_length=255, choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('BANNED', 'Banned'), ('ARCHIVED', 'Archived')])
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    privacy = models.CharField(max_length=255, choices=[('PUBLIC', 'Public'), ('HIDDEN', 'Hidden'), ('RESTRICTED', 'Restricted')])
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title