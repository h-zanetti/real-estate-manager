import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.users.models import User

# Registro
@pytest.fixture
def resposta_registro(client, db):
    resp = client.post(reverse('registro'), data={
        'email': 'endereco_de@email.com',
        'password1': 'testUser123',
        'password2': 'testUser123'
    })

    return resp

def test_registro_status_code(resposta_registro):
    assert resposta_registro.status_code == 302

def test_usuario_existe_no_bd(resposta_registro):
    assert User.objects.exists()

# Seja um anfitrião
@pytest.fixture
def resposta_ser_anfitriao(client):
    return client.post(reverse('ser_anfitriao'), data={
        'email': 'test@email.com',
        'assunto': 'Quero ser um Anfitrião',
        'mensagem': 'Olá, tenho um imóvel e quero fazer dinheiro!'
    })

def test_ser_anfitriao_status_code(resposta_ser_anfitriao):
    assert resposta_ser_anfitriao.status_code == 302
