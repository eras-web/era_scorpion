from django.db import models
from .user_model import User
from django.utils import timezone


class Game(models.Model):  # Наследуем от models.Model
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,null=True, blank=True)
    platform = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now)
    description = models.TextField(default='Описание...')
    users = models.ManyToManyField(User, related_name='games')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'core'  
