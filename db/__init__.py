import os

from dotenv import load_dotenv


load_dotenv()

connection_format = "mongodb://{}:{}@{}/{}"
address = os.getenv("ADDRESS")
database_name = "printers_db"
