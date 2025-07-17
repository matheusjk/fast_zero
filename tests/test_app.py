from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():

    """Testa se a rota raiz retorna status 200 e a mensagem 'Olá mundo'."""

    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': "Olá mundo"}  # Assert (verificação)
    # Verifica se a resposta JSON contém a mensagem esperada
    # e se o status code é 200 (OK).
