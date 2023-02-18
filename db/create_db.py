from db.mongo_creator import MongoCreator


def create_db() -> None:
    mongo = MongoCreator()
    mongo.create_collections()
    mongo.create_roles()
