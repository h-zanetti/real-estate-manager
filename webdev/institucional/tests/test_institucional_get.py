from django.urls import reverse

def test_home_status_code(client):
    resposta = client.get(reverse('institucional:home'))
    assert resposta.status_code == 200

def test_quem_somos_status_code(client):
    resposta = client.get(reverse('institucional:quem_somos'))
    assert resposta.status_code == 200
