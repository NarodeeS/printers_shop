import os
import pymongo
from dotenv import load_dotenv


load_dotenv()


class Mongo:
    username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    address = os.getenv("ADDRESS")
    
    def __init__(self) -> None:
        connection_string = f'mongodb://{Mongo.username}:{Mongo.password}@{Mongo.address}/printers?retryWrites=true'
        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database()
