import pytest
from pymongo.errors import WriteError

from db.mongo_client import MongoClient
from db.mongo_creator import MongoCreator


try:
    MongoCreator().create_user("how", "pass", "admin")
except Exception:
    pass

client = MongoClient("how", "pass")


def test_client_adding_error():
    with pytest.raises(WriteError):
        incorrect_data = {"name": "george", "phone": 2944, "email": "george@mail.ru"}
        client.db.clients.insert_one(incorrect_data)


def test_client_adding():
    incorrect_data = {
        "name": "george",
        "phone": "88005553535",
        "email": "george@mail.ru",
    }
    client.db.clients.insert_one(incorrect_data)
