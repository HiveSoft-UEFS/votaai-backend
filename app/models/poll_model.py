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
    code = models.SmallIntegerField(blank=True, null=True, unique=True)
    category = models.CharField(max_length=255, choices=[('ENTERTAINMENT','entertainment'), ('TECHNOLOGY','technology'), ('SPORTS','sports'), ('FOOD','food'), ('TOURISM','tourism'), ('CULTURE','culture'), ('ART','art') ,('POLITICS','politics'), ('SCIENCE','science'), ('FASHION','fashion'), ('CURIOSITIES','curiosities'), ('RANDOM', 'random')], default='random')
    tags = models.CharField(max_length=255, blank=True, help_text="Coloque as telas separadas por #")

    @property
    # def save(self, *args, **kwargs):
    #     if self.privacy == 'RESTRICTED' and self.code is None:
    #         raise ValueError("O campo 'code' é obrigatório quando privacy é 'RESTRICTED'.")
    #     if self.privacy != 'RESTRICTED':
    #         self.code = None  
    #     super().save(*args, **kwargs)
        
    def questions(self):
        return self.questionfield_set.all()

    def __str__(self):
        return self.title