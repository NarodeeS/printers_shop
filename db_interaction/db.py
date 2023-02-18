import os
import json

import pymongo
from pymongo.errors import PyMongoError
from dotenv import load_dotenv


load_dotenv()


connection_format = "mongodb://{}:{}@{}/{}"
address = os.getenv("ADDRESS")
database_name = "printers_db"


class MongoCreator:
    """Mongo database creation class"""

    username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    collections_data_file = "db_interaction/data/collections_data.json"
    roles_data_file = "db_interaction/data/roles_data.json"

    def __init__(self) -> None:
        connection_string = connection_format.format(
            self.username, self.password, address, database_name
        )
        connection_string += "?authSource=admin"
        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database(database_name)

    def create_collections(self) -> None:
        for collection_data in self._get_json_data(self.collections_data_file): 
            try:
                self.db.create_collection(
                    collection_data["collection_name"],
                    validator=collection_data["validator"],
                )
            except PyMongoError as e:
                print(e)
                return
    
    def create_roles(self) -> None:
        for role_data in self._get_json_data(self.roles_data_file):
            try:
                self.db.command("createRole", role_data["role"], 
                                privileges=role_data["privileges"],
                                roles=[]
                )
            except PyMongoError as e:
                print(e)
        
    def _get_json_data(self, path: str) -> list:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)


class MongoClient:
    """Class for with mongo database"""

    def __init__(self, username: str, password: str) -> None:
        connection_string = connection_format.format(
            username, password, address, database_name
        )
        client = pymongo.MongoClient(connection_string)
        self._db = client.get_database(database_name)
