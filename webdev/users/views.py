from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, 'Seu usuário foi criado com sucesso!')
            return redirect('institucional:home')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'users/registro.html', context)

def login_view(request):
    pass

def logout(request):
    pass
