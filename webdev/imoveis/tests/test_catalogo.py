from pytest_django.asserts import assertContains
from webdev.imoveis.models import Imovel
import pytest
from django.urls import reverse

@pytest.fixture
def imovel(db):
    return Imovel.objects.create(
        ponto_de_referencia='Maresias',
        cidade='São Sebastião',
        estado='SP',
        endereco='Av. Frente da Praia, 123, 01100-000',
        ocupacao_maxima=6,
        diaria=250
    )

@pytest.fixture
def resposta_catalogo(client, imovel):
    return client.get(reverse('imoveis:catalogo'))

def test_catalogo_status_code(resposta_catalogo):
    assert resposta_catalogo.status_code == 200

# def test_imovel_presente(resposta_catalogo, imovel):
#     assertContains(
#         resposta_catalogo,
#         f'<a href="{reverse("imoveis:agendar_estadia", kwargs={"imovel_id": imovel.id})}"'
#     )