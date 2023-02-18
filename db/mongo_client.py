import pymongo

from db import *


class MongoClient:
    """Class for with mongo database"""

    def __init__(self, username: str, password: str) -> None:
        connection_string = connection_format.format(
            username, password, address, database_name
        )
        client = pymongo.MongoClient(connection_string)
        self._db = client.get_database(database_name)
