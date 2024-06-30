from django.db import models
from .user_model import User
from .poll_model import Poll


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True, blank=True)