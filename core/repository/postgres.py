from core.model.user_model import User
from core.model.user_model import User
from django.db.models import Q

def filter_users(query=None):
    if query:
        return User.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
    return User.objects.all()

def get_all_users():
    return User.objects.all()

def create_user(data):
    return User.objects.create(**data)
