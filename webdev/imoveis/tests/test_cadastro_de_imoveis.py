from pytest_django.asserts import assertContains
from django.urls import reverse
from webdev.imoveis.models import Imovel
from webdev.users.models import User
import pytest

@pytest.fixture
def user(db):
    return User.objects.create(
        email='endereco_de@email.com',
        password='TestUser123'
    )

# GET
@pytest.fixture
def resposta_cadastrar_imovel_get(client, user):
    client.force_login(user)
    return client.get(reverse('imoveis:cadastrar_imovel'))

def test_cadastrar_imovel_get_status_code(resposta_cadastrar_imovel_get):
    assert resposta_cadastrar_imovel_get.status_code == 200

def test_form_presente(resposta_cadastrar_imovel_get):
    assertContains(
        resposta_cadastrar_imovel_get,
        f'<form action="{reverse("imoveis:cadastrar_imovel")}"'
    )

def test_btn_submit_presente(resposta_cadastrar_imovel_get):
    assertContains(resposta_cadastrar_imovel_get, '<button type="submit"')

# POST
@pytest.fixture
def resposta_cadastrar_imovel(client, user):
    client.force_login(user)
    return client.post(reverse('imoveis:cadastrar_imovel'), data={
        'ponto_de_referencia': 'Maresias',
        'cidade': 'São Sebastião',
        'estado': 'SP',
        'endereco': 'Av. Frente da Praia, 123, 01100-000',
        'ocupacao_maxima': 6,
        'diaria': 250
    })

def test_cadastrar_imovel_status_code(resposta_cadastrar_imovel):
    assert resposta_cadastrar_imovel.status_code == 302

def test_imovel_cadastrado(resposta_cadastrar_imovel):
    assert Imovel.objects.exists()
