from django import forms

class FilmSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label="Атауы")
    year = forms.IntegerField(required=False, label="Жыл")
    genre = forms.CharField(max_length=100, required=False, label="Жанры")
    rating = forms.FloatField(required=False, label="Рейтинг (0-10)", min_value=0, max_value=10)
