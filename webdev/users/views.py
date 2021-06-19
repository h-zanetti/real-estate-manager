from django.core.mail import EmailMessage
from webdev.imoveis.models import Reserva
from django.http.response import Http404
from webdev.users.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EnviarEmailForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Seu usuário foi criado com sucesso!')
            return redirect('imoveis:catalogo')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'users/registro.html', context)

def ser_anfitriao(request):
    if request.method == 'POST':
        form = EnviarEmailForm(request.POST)
        if form.is_valid():
            email = EmailMessage(
                form.cleaned_data.get('assunto'),
                form.cleaned_data.get('mensagem'),
                to=['contato@agahsolutions.com', 'henriaguiar99@gmail.com']
            )
            if email.send():
                messages.success(request, 'Pedido enviado com sucesso! Verifique seu email com os detalhes da aplicação.')
                if not request.user.is_authenticated:
                    return redirect('registro')
                else:
                    return redirect('imoveis:acomodacoes')
            else:
                messages.error(request, 'Houve um erro no envio da aplicação.')
                return redirect('ser_anfitriao')
    else:
        form = EnviarEmailForm()

    context = {
        'form': form
    }
    return render(request, 'users/ser_anfitriao.html', context)

@login_required
def minhas_reservas(request):
    try:
        user = User.objects.get(id=request.user.id)
        context = {
            'reservas': Reserva.objects.filter(hospede=user)
        }
        return render(request, 'users/minhas_reservas.html', context)
    except User.DoesNotExist:
        raise Http404('Usuário não encontrado')
