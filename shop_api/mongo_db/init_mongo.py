from  mongo_db.mongo_client import MongoClientHandler


def init_categories():
    client = MongoClientHandler()
    if len(list(client.db.categories.find({}))) == 0:
        client.db.categories.insert_many([
            {
                "name": "Лазерный"
            },
            {
                "name": "Светодиодный"
            },
            {
                "name": "Струйный"
            }
        ])
