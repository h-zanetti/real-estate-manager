from pytest_django.asserts import assertContains
import pytest
from django.urls import reverse
def test_home_status_code(client):
    resposta = client.get(reverse('institucional:home'))
    assert resposta.status_code == 200


@pytest.fixture
def resposta_quem_somos(client):
    return client.get(reverse('institucional:quem_somos'))

def test_quem_somos_status_code(resposta_quem_somos):
    assert resposta_quem_somos.status_code == 200

def test_btn_ser_anfitriao_presente(resposta_quem_somos):
    assertContains(resposta_quem_somos, f'<a href="{reverse("ser_anfitriao")}"')

def test_btn_catalogo_presente(resposta_quem_somos):
    assertContains(resposta_quem_somos, f'<a href="{reverse("imoveis:catalogo")}"')
