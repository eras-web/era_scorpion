from django.urls import path
from core.views import home, FilmListView, user_list, login_view, register

urlpatterns = [
    path('', home, name='home'),
    path('films/', FilmListView.as_view(), name='films'),
    path('users/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]
