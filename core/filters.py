import django_filters
from .models import Film

class FilmFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="Атауы", lookup_expr='icontains')
    year = django_filters.NumberFilter(label="Жылы")
    genre = django_filters.ChoiceFilter(choices=Film.GENRE_CHOICES, label="Жанр")
    rating = django_filters.RangeFilter(label="Рейтинг (аралығы)")

    class Meta:
        model = Film
        fields = ['title', 'year', 'genre', 'rating']
