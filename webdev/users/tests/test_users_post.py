import pytest
from django.contrib import auth
from django.urls import reverse
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

# Login
@pytest.fixture
def usuario(db):
    return User.objects.create(
        email='endereco_de@email.com',
        password='testUser123',
    )
