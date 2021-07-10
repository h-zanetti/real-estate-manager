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

# Gerenciador de imóveis
@pytest.fixture
def resposta_gerenciar_imoveis(client, imovel, user):
    client.force_login(user)
    return client.get(reverse('imoveis:gerenciar_imoveis'))

def test_gerenciar_imoveis_status_code(resposta_gerenciar_imoveis):
    assert resposta_gerenciar_imoveis.status_code == 200

def test_btn_gerenciar_imoveis_presente(resposta_gerenciar_imoveis):
    assertContains(resposta_gerenciar_imoveis, f'<a href="{reverse("imoveis:gerenciar_imoveis")}"')

def test_btn_editar_imovel_presente(resposta_gerenciar_imoveis, imovel):
    assertContains(
        resposta_gerenciar_imoveis,
        f'<a href="{reverse("imoveis:editar_imovel", kwargs={"imovel_id": imovel.id})}"'
    )

def test_btn_deletar_imovel_presente(resposta_gerenciar_imoveis, imovel):
    assertContains(
        resposta_gerenciar_imoveis,
        f'<form action="{reverse("imoveis:deletar_imovel", kwargs={"imovel_id": imovel.id})}"'
    )

def test_imovel_presente(resposta_gerenciar_imoveis, imovel):
    assertContains(
        resposta_gerenciar_imoveis,
        f'<a href="{reverse("imoveis:agendar_estadia", kwargs={"imovel_id": imovel.id})}"'
    )

# Edição de imóveis
@pytest.fixture
def get_editar_imovel(client, imovel, user):
    client.force_login(user)
    return client.get(reverse(
        'imoveis:editar_imovel',
        kwargs={'imovel_id': imovel.id}
    ))

def test_editar_imovel_status_code(get_editar_imovel):
    assert get_editar_imovel.status_code == 200

@pytest.fixture
def post_editar_imovel(client, imovel, user):
    client.force_login(user)
    return client.post(
        reverse('imoveis:editar_imovel', kwargs={'imovel_id': imovel.id}),
        data={
            'anfitriao': user.id,
            'ponto_de_referencia': 'Maresias',
            'cidade': 'São Sebastião',
            'estado': 'SP',
            'endereco': 'Av. Frente da Praia, 123, 01100-000',
            'ocupacao_maxima': 10,
            'diaria': 250
        },
    )

# def test_form_sem_erros(post_editar_imovel):
#     assert not post_editar_imovel.context['form'].errors

def test_editar_imovel_status_code(post_editar_imovel):
    assert post_editar_imovel.status_code == 302

def test_imovel_editado(post_editar_imovel):
    assert Imovel.objects.first().ocupacao_maxima == 10

# Deleção de imóveis
@pytest.fixture
def deletar_imovel(client, imovel, user):
    client.force_login(user)
    return client.post(reverse(
        'imoveis:deletar_imovel',
        kwargs={'imovel_id': imovel.id}
    ))

def test_deletar_imovel_status_code(deletar_imovel):
    assert deletar_imovel.status_code == 302

def test_imovel_editado(deletar_imovel):
    assert not Imovel.objects.exists()
