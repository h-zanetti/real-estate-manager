from webdev.imoveis.models import Imovel
from django.http.response import Http404, HttpResponse
from django.shortcuts import render

def catalogo(request):
    context = {
        'imoveis': Imovel.objects.all(),
    }
    return render(request, 'imoveis/catalogo.html', context)

# def agendar_estadia(request, imovel_id):
#     try:
#         imovel = Imovel.objects.get(id=imovel_id)
#         context = {
#             'imovel': imovel
#         }
#         return render(request, 'imoveis/agendar_estadia.html', context)
#     except Imovel.DoesNotExist:
#         raise Http404('Imóvel não encontrado')
