from django import forms
from core.model.game_model import Game
from core.model.user_model import User

class GameForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Game
        fields = ['title', 'genre', 'platform', 'release_date', 'description', 'users']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'users': forms.CheckboxSelectMultiple()  # если нужно выбрать нескольких пользователей
        }