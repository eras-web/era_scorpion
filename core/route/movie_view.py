from django.shortcuts import render, redirect
from core.repository.aerospike import filter_games, insert_game
from core.forms.game_form import GameForm

def game_list(request):
    query = request.GET.get('q')
    games = filter_games(query)

    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            insert_game(data['game_id'], {
                "name": data['name'],
                "category": data['category']
            })
            return redirect('game_list')
    else:
        form = GameForm()

    return render(request, "games.html", {"games": games, "form": form, "query": query})
