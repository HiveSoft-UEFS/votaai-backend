from django.db import models
from .userModel import User
from .pollModel import Poll

class Whitelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)