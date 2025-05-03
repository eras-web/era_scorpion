from django import forms
from core.model.user_model import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'city', 'education', 'bio']
