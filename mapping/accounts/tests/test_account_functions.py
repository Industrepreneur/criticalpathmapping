import pytest


def test_login_page_exists(client):
    response = client.get('/login/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_with_valid_credentials_works(client):
    response = client.post('/login/', {
        'username': 'robin@robinbolton.com',
        'password': 'robin'
    })
    assert response.status_code == 200

    response = client.get('/admin/')
    # assert response.status_code == 200

    # print(response.content)
    # assert response.content == 'development'
