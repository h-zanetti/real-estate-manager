import pytest
from pytest_django.asserts import assertContains, assertRedirects
from django.urls import reverse
from webdev.users.models import User
from webdev.imoveis.models import Imovel, Reserva

@pytest.fixture
def host(db):
    return User.objects.create(
        email='host@email.com',
        password='testUser123',
        is_host=True
    )

@pytest.fixture
def imovel(host):
    return Imovel.objects.create(
        anfitriao=host,
        ponto_de_referencia='Maresias',
        cidade='São Sebastião',
        estado='SP',
        endereco='Av. Frente da Praia, 123, 01100-000',
        ocupacao_maxima=6,
        diaria=250
    )

@pytest.fixture
def user(db):
    return User.objects.create(
        email='endereco_de@email.com',
        password='testUser123',
    )

@pytest.fixture
def reserva(imovel, user):
    return Reserva.objects.create(
        imovel=imovel,
        hospede=user,
        check_in='2021-04-04',
        check_out='2021-04-14',
        visitantes=2
    )

# Testar lista de reservas
@pytest.fixture
def resposta_reservas(client, user, reserva):
    client.force_login(user)
    return client.get(reverse('minhas_reservas',))

def test_btn_minhas_reservas_presente(resposta_reservas, user):
    assertContains(
        resposta_reservas,
        f'<a href="{reverse("minhas_reservas")}"'
    )
def test_minhas_reservas_status_code(resposta_reservas):
    assert resposta_reservas.status_code == 200

def test_reserva_presente(resposta_reservas, imovel):
    assertContains(resposta_reservas, imovel.ponto_de_referencia)

# Negar o cadastro de imóveis por usuários que não são host
@pytest.fixture
def resposta_cadastrar_imovel_com_guest(client, user):
    client.force_login(user)
    return client.get(reverse('imoveis:cadastrar_imovel'))

def test_redirecionamento(resposta_cadastrar_imovel_com_guest):
    assertRedirects(
        resposta_cadastrar_imovel_com_guest,
        reverse('ser_anfitriao')
    )

# Cadastro de imóveis por hosts
@pytest.fixture
def resposta_cadastrar_imovel_com_host(client, host):
    client.force_login(host)
    return client.get(reverse('imoveis:cadastrar_imovel'))

def test_form_presente(resposta_cadastrar_imovel_com_host):
    assertContains(
        resposta_cadastrar_imovel_com_host,
        f'<form action="{reverse("imoveis:cadastrar_imovel")}"'
    )

def test_btn_submit_presente(resposta_cadastrar_imovel_com_host):
    assertContains(
        resposta_cadastrar_imovel_com_host,
        '<button type="submit"'
    )

