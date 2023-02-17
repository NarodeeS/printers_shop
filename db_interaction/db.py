import os
import json
import dotenv
import pymongo
from dotenv import load_dotenv


load_dotenv()


connection_format = "mongodb://{}:{}@{}/{}"
address = os.getenv("ADDRESS")
database_name = "printers"


class MongoCreator:
    """Mongo database creation class"""

    username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    collections_data_file = "./collections_data.json"

    def __init__(self) -> None:
        connection_string = connection_format.format(
            self.username, self.password, address, database_name
        )
        connection_string += "?authSource=admin"
        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database(database_name)
        self._create_collections()
        self._create_roles()

    def _create_collections(self) -> None:
        with open(self.collections_data_file, "r") as file:
            collections_data = json.load(file)

        for collection_data in collections_data:
            self.db.create_collection(
                collection_data["collection_name"],
                validator=collection_data["validator"],
            )

    def _create_roles(self) -> None:
        role_name = "worker"
        self.db.command(
            "createRole",
            role_name,
            privileges=[{"resource": {"cluster": True}, "actions": ["inprog"]}],
            roles=[],
        )


class MongoClient:
    """Class for with mongo database"""

    def __init__(self, username: str, password: str) -> None:
        connection_string = connection_format.format(
            username, password, address, database_name
        )
        client = pymongo.MongoClient(connection_string)
        self._db = client.get_database(database_name)
