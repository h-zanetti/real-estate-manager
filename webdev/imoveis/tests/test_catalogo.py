from webdev.users.models import User
from pytest_django.asserts import assertContains
from webdev.imoveis.models import Imovel
import pytest
from django.urls import reverse

@pytest.fixture
def user(db):
    return User.objects.create(
        email='endereco_de@email.com',
        password='testUser123',
        is_host=True,
    )

@pytest.fixture
def imovel(user):
    return Imovel.objects.create(
        anfitriao=user,
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

def test_btn_catalogo_presente(resposta_catalogo):
    assertContains(resposta_catalogo, f'<a href="{reverse("imoveis:catalogo")}"')

def test_imovel_presente(resposta_catalogo, imovel):
    assertContains(
        resposta_catalogo,
        f'<a href="{reverse("imoveis:agendar_estadia", kwargs={"imovel_id": imovel.id})}"'
    )