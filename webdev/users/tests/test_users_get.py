import pytest
from django.contrib import auth
from django.urls import reverse
from webdev.users.models import User
from pytest_django.asserts import assertContains

# Registro
@pytest.fixture
def resposta_registro(client):
    resp = client.get(reverse('registro'))
    return resp

def test_registro_status_code(resposta_registro):
    assert resposta_registro.status_code == 200

def test_formulario_de_registro_presente(resposta_registro):
    assertContains(resposta_registro, '<form')

def test_btn_salvar_presente(resposta_registro):
    assertContains(resposta_registro, '<button type="submit"')

@pytest.fixture
def usuario(db):
    return User.objects.create(
        email='endereco_de@email.com',
        password='testUser123',
    )

# Login
@pytest.fixture
def resposta_login(client):
    resp = client.get(reverse('login'))
    return resp

def test_login_status_code(resposta_login):
    assert resposta_login.status_code == 200

def test_formulario_de_login_presente(resposta_login):
    assertContains(resposta_login, '<form')

def test_input_username_presente(resposta_login):
    # Apesar do usuário ser logado com seu endereço de email, a classe LoginView do django chama esse input de username 
    assertContains(resposta_login, '<input type="text" name="username"')

def test_btn_enviar_presente(resposta_login):
    assertContains(resposta_login, '<button type="submit"')


# Logout
@pytest.fixture
def resposta_logout(client, usuario):
    client.login(
        email='endereco_de@email.com',
        password='testUser123',
    )
    resp = client.get(reverse('logout'))
    return resp

def test_logout_status_code(resposta_logout):
    assert resposta_logout.status_code == 302

def test_usuario_nao_autenticado(resposta_logout):
    assert auth.get_user(resposta_logout.client).is_anonymous

# Botões presente
@pytest.fixture
def resposta_home_logado(client, usuario):
    client.force_login(usuario)
    resp = client.get('/')
    return resp

def test_btn_logout_presente(resposta_home_logado):
    assertContains(resposta_home_logado, f'<a href="{reverse("logout")}"')

@pytest.fixture
def resposta_home_anonimo(client):
    return client.get('/')

def test_btn_login_presente(resposta_home_anonimo):
    assertContains(resposta_home_anonimo, f'<a href="{reverse("login")}"')
