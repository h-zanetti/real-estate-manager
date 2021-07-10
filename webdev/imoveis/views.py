from django.contrib import messages
from django.contrib.auth.decorators import login_required
from webdev.imoveis.forms import ReservaForm, ImovelForm
from webdev.imoveis.models import Foto, Imovel
from django.http.response import Http404, HttpResponseForbidden
from django.shortcuts import redirect, render

def catalogo(request):
    context = {
        'imoveis': Imovel.objects.all(),
    }
    return render(request, 'imoveis/catalogo.html', context)

@login_required
def cadastrar_imovel(request):
    if request.user.is_host:
        if request.method == 'POST':
            form = ImovelForm(request.POST, initial={'anfitriao': request.user.id})
            if form.is_valid():
                imovel = form.save()
                foto = Foto.objects.get(nome='default')
                imovel.fotos.add(foto)
                return redirect('imoveis:catalogo')
        else:
            form = ImovelForm(initial={'anfitriao': request.user.id})
        
        context = {
            'title': 'Cadastrar imóvel',
            'form': form
        }
        return render(request, 'imoveis/imovel_form.html', context)
    else:
        messages.warning(request, 'Torne-se um anfitrião e cadastre seus imóveis!')
        return redirect('ser_anfitriao')

@login_required
def editar_imovel(request, imovel_id):
    try:
        imovel = Imovel.objects.get(id=imovel_id)
        if imovel.anfitriao == request.user:
            if request.method == 'POST':
                form = ImovelForm(request.POST, instance=imovel)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Imóvel alterado com sucesso!')
                    return redirect('imoveis:gerenciar_imoveis')
            else:
                form = ImovelForm(instance=imovel)
            
            context = {
                'title': 'Editar Imóvel',
                'form': form
            }
            return render(request, 'imoveis/imovel_form.html', context)
        else:
            return HttpResponseForbidden()
    except Imovel.DoesNotExist:
        raise Http404("Imóvel não encontrado.")

@login_required
def deletar_imovel(request, imovel_id):
    try:
        imovel = Imovel.objects.get(id=imovel_id)
        if request.user == imovel.anfitriao:
            if request.method == 'POST':
                imovel.delete()
                messages.success(request, "Imóvel deletado com sucesso.")
                return redirect('imoveis:gerenciar_imoveis')
        else:
            return HttpResponseForbidden()
    except:
        raise Http404("Imóvel não encontrado")

def agendar_estadia(request, imovel_id):
    try:
        imovel = Imovel.objects.get(id=imovel_id)
        if request.user.is_authenticated:
            initial = {
                'imovel': imovel,
                'user': request.user,
                'nome_completo': request.user.get_full_name(),
                'email': request.user.email,
            }
        else:
            initial = {'imovel': imovel}
        if request.method == 'POST':
            form = ReservaForm(request.POST, initial=initial)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = ReservaForm(initial=initial)

        context = {
            'imovel': imovel,
            'form': form
        }
        return render(request, 'imoveis/agendar_estadia.html', context)

    except Imovel.DoesNotExist:
        raise Http404('Imóvel não encontrado')

@login_required
def gerenciar_imoveis(request):
    if request.user.is_host:
        imoveis = Imovel.objects.filter(anfitriao=request.user)
        return render(request, 'imoveis/gerenciar_imoveis.html', {'imoveis': imoveis})

    else:
        messages.success(request, "É necessário se tornar um anfitrião para adicinar imóveis. Envie-nos uma mensagem e entraremos em contato assim que possível.")
        return redirect('ser_anfitriao')