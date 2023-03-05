import os
from typing import NamedTuple

import pytest
import httpx


API_ADDRESS = f'{os.getenv("API_ADDRESS")}/api'
if not API_ADDRESS:
    exit()


class Category(NamedTuple):
    id: str
    name: str


def get_test_category_id() -> Category:
    response = httpx.get(f'{API_ADDRESS}/categories/')
    return Category(**response.json())


@pytest.fixture
def get_user_creation_data() -> dict:
    return {
        "name": "george",
        "phone": "88005553535",
        "email": "george@mail.ru",
    }


@pytest.fixture
def printer_creation_data() -> dict:
    return {
        'manufacturer': 'HP',
        'printer_name': 'test name',
        'paper_weight': 123,
        'colors_number': 4,
        'resolution:': '121',
        'print_speed': 12,
        'cartridge_count': 3 ,
        'tray_capacity': 100,
        'paper_format': 'A4',
        'category_id': get_test_category_id().id,
        'amount': 12,
        'price': 12
    }
