from pytest_django.asserts import assertContains
from django.urls import reverse
from webdev.imoveis.models import Imovel, Reserva
import pytest

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

# GET
@pytest.fixture
def resposta_agendar_estadia(client, imovel):
    return client.get(reverse(
        'imoveis:agendar_estadia',
        kwargs={'imovel_id': imovel.id}
    ))

def test_agendar_estadia_status_code(resposta_agendar_estadia):
    assert resposta_agendar_estadia.status_code == 200

def test_form_presente(resposta_agendar_estadia, imovel):
    assertContains(
        resposta_agendar_estadia,
        f'<form action="{reverse("imoveis:agendar_estadia", kwargs={"imovel_id": imovel.id})}"'
    )

def test_btn_submit_presente(resposta_agendar_estadia):
    assertContains(resposta_agendar_estadia, '<button type="submit"')

# POST
@pytest.fixture
def resposta_agendar_estadia_post(client, imovel):
    return client.post(
        reverse('imoveis:agendar_estadia', kwargs={'imovel_id': imovel.id}),
        data = {
            'user': '',
            'imovel': imovel.id,
            'nome_completo': 'José da Silva',
            'email': 'jose.silva@gmail.com',
            'telefone': '11944647444',
            'check_in': '01-04-2021',
            'check_out': '05-04-2021',
            'visitantes': 5,
        }
    )

def test_agendar_estadia_post_status_code(resposta_agendar_estadia_post):
    assert resposta_agendar_estadia_post.status_code == 302

# def test_nenhum_form_error(resposta_agendar_estadia_post):
#     assert not resposta_agendar_estadia_post.context['form'].errors

def test_reserva_criada(resposta_agendar_estadia_post):
    assert Reserva.objects.exists()