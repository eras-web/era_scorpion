from django.contrib import admin
from django.urls import path
from core.views import home, FilmListView, user_list, login_view, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('films/', FilmListView.as_view(), name='film_list'),
    path('users/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]
