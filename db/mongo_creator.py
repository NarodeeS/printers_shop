import os
import json
from pathlib import Path

import pymongo
from pymongo.errors import PyMongoError
from db.mongo_client import MongoClient

from db import *


class MongoCreator:
    """Mongo database creation class"""

    username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    collections_data_file = Path(__file__).parent / "data/collections_data.json"
    roles_data_file = Path(__file__).parent / "data/roles_data.json"

    def __init__(self) -> None:
        connection_string = connection_format.format(
            self.username, self.password, address, database_name
        )

        connection_string += "?authSource=admin"

        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database(database_name)

    def create_collections(self) -> None:
        for collection_data in self._get_json_data(str(self.collections_data_file)):
            try:
                self.db.create_collection(
                    collection_data["collection_name"],
                    validator=collection_data["validator"],
                )
            except PyMongoError as e:
                print(e)
                return

    def create_user(self, username: str, password: str, role: str) -> MongoClient:
        if self._user_exists(username):
            raise PyMongoError("User already exists")
        if not self._role_exists(role):
            raise PyMongoError("No such role")
        self.db.command(
            "createUser",
            username,
            pwd=password,
            roles=[{"role": role, "db": database_name}],
        )
        return MongoClient(username, password)

    def _user_exists(self, username: str) -> bool:
        user_objects = self.db.command("usersInfo")["users"]
        return username in [user_object["user"] for user_object in user_objects]

    def _role_exists(self, role: str) -> bool:
        roles_objects = self.db.command("rolesInfo")["roles"]
        print(roles_objects)
        return role in [role_object["role"] for role_object in roles_objects]

    def _get_json_data(self, path: str) -> list:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def create_roles(self) -> None:
        for role_data in self._get_json_data(str(self.roles_data_file)):
            try:
                self.db.command(
                    "createRole",
                    role_data["role"],
                    privileges=role_data["privileges"],
                    roles=[],
                )
            except PyMongoError as e:
                print(e)
