import httpx

from conftest import API_ADDRESS


def test_get_all_categories():
    print(f'{API_ADDRESS}/categories/')
    response = httpx.get(f'{API_ADDRESS}/categories/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
