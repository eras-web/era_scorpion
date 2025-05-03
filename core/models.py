from django.db import models

class Film(models.Model):
    GENRE_CHOICES = [
        ('drama', 'Драма'),
        ('comedy', 'Комедия'),
        ('action', 'Экшн'),
        ('history', 'Тарихи'),
        ('fantasy', 'Фантастика'),
    ]

    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
