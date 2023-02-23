import os


connection_format = "mongodb://{}:{}@mongodb:27017/{}"
database_name = os.getenv("MONGO_DB")
