from db import MongoCreator

def create_db() -> None:
    mongo = MongoCreator()
    mongo.create_collections()
    mongo.create_roles()


if __name__ == "__main__":
    create_db()
