import pytest
from django.urls import reverse
from webdev.users.models import User

@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('users:registro'), data={
        'email': 'tita@gmail.com',
        'password1': 'Zanetti.',
        'password2': 'Zanetti.'
    })

    return resp

def test_usuario_existe_no_bd(resposta):
    assert User.objects.exists()