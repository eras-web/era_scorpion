from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_filters.views import FilterView
from .models import Film
from .filters import FilmFilter


# Басты бет
def home(request):
    return render(request, 'core/home.html')

from django.shortcuts import render
from .models import Film

def film_list(request):
    title = request.GET.get('title', '')
    year = request.GET.get('year', '')
    rating = request.GET.get('rating', '')

    films = Film.objects.all()

    if title:
        films = films.filter(title__icontains=title)

    if year:
        films = films.filter(year__icontains=year)

    if rating:
        try:
            rating_value = float(rating)
            films = films.filter(rating__gte=rating_value)
        except ValueError:
            pass  # Егер сан болмаса, фильтр қолданылмайды

    return render(request, 'core/films.html', {'films': films})



# Фильмдер беті (модельмен және фильтрмен)
class FilmListView(FilterView):
    model = Film
    filterset_class = FilmFilter
    template_name = 'core/films.html'
    context_object_name = 'films'


# Пайдаланушылар тізімі
def user_list(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'core/users.html', {'users': users, 'form': form})


# Тіркелу
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


# Кіру
def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = 'Пайдаланушы аты немесе құпиясөз қате!'
    return render(request, 'core/login.html', {'error': error})
