from django.db import models


class RecoveryToken(models.Model):
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
