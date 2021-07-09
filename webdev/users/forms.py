from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf', 'email', 'phone_number')

class EnviarEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'nome@email.com'}), label="Endereço de Email")
    assunto = forms.CharField(max_length=50, label="Assunto", initial="Quero ser um Anfitrião")
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Conte-nos um pouco sobre seu imóvel e seus objetivos!'}), label="Mensagem")
