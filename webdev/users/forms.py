from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf', 'email', 'phone_number')
