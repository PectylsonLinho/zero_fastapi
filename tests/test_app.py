from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


<<<<<<< HEAD
def test_root_deve_retormar_oke_e_ola_mundo():
=======
def test_root_deve_retormar_ok_e_ola_mundo():
>>>>>>> ac57a08fd926895011e9b88e6cb2d9bda3a5c4f9
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
