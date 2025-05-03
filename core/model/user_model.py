from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=150)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        app_label = 'core'

