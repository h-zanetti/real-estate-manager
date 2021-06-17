from django.contrib.auth.decorators import login_required
from webdev.imoveis.forms import ImovelForm
from webdev.imoveis.models import Imovel
from django.http.response import Http404
from django.shortcuts import redirect, render

def catalogo(request):
    context = {
        'imoveis': Imovel.objects.all(),
    }
    return render(request, 'imoveis/catalogo.html', context)

@login_required
def cadastrar_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imoveis:catalogo')
    else:
        form = ImovelForm()
    
    context = {
        'form': form
    }
    return render(request, 'imoveis/cadastrar_imovel.html', context)

# def agendar_estadia(request, imovel_id):
#     try:
#         imovel = Imovel.objects.get(id=imovel_id)
#         context = {
#             'imovel': imovel
#         }
#         return render(request, 'imoveis/agendar_estadia.html', context)
#     except Imovel.DoesNotExist:
#         raise Http404('Imóvel não encontrado')
