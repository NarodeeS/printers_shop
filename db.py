import os
import pymongo
from dotenv import load_dotenv


load_dotenv()
username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
address = os.getenv("ADDRESS")

connection_string = f'mongodb://{username}:{password}@{address}/printers?retryWrites=true'
client = pymongo.MongoClient(connection_string)
db = client.get_database()
