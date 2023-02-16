import os
import json
import pymongo
from dotenv import load_dotenv


load_dotenv()


class Mongo:
    username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    address = os.getenv("ADDRESS")
    database_name = 'printers'
    collections_data_file = './collections_data.json'
    
    def __init__(self) -> None:
        connection_string = f'mongodb://{self.username}:{self.password}@{self.address}/{self.database_name}?retryWrites=true'
        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database()
        # self._create_collections()

    def _create_collections(self) -> None:
        with open('collections_data_file', 'r') as file:
            collections_data = json.load(file)
            
        for collection_data in collections_data:
            self.db.create_collection(collection_data['collection_name'], 
                                      validator=collection_data['validator'])
