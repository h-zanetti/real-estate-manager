import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    resp = client.get(reverse('users:registro'))
    return resp

def test_registro_status_code(resposta):
    assert resposta.status_code == 200

def test_formulario_de_registro_presente(resposta):
    assertContains(resposta, '<form')

def test_btn_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')

