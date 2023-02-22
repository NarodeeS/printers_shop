import datetime

import pymongo
from bson.objectid import ObjectId
from pymongo.cursor import Cursor

from . import *


class MongoClientHandler:
    """Class for work with mongo database"""
    
    username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    
    def __init__(self ) -> None:
        connection_string = connection_format.format(
            self.username, self.password, address, database_name
        )
        connection_string += f"?authSource=admin" # {database_name}

        client = pymongo.MongoClient(connection_string)
        self.db = client.get_database(database_name)

    def find_printer(self, queue: dict) -> dict | Cursor:
        try:
            rez = self.db.printers.find(queue)
            return rez
        except Exception as e:
            return {"error": e}

    def add_printer_to_orders(self, phone: str, queue: dict) -> None | dict:
        chosen_printer = self.db.printers.find_one(queue)
        if type(chosen_printer) is dict:
            try:
                client_id = self.db.clients.find_one({"phone": phone})
                product_id = self.db.printers.find_one(queue)

                if client_id is None:
                    return {"no such element": "client_id"}
                if product_id is None:
                    return {"no such element": "product_id"}

                insert_queue = {
                    "client_id": ObjectId(str(client_id["_id"])),
                    "status": "created",
                    "products": [
                        {
                            "product_id": ObjectId(str(product_id["_id"])),
                            "amount": 1,
                        }
                    ],
                    "date": datetime.datetime.utcnow(),
                }
                self.db.orders.insert_one(insert_queue)
            except Exception as e:
                return {"error": e}

    def get_order_price(self, phone: str) -> dict | int:
        user = self.db.clients.find_one({"phone": phone})
        bascket_counter = 0

        if user is None:
            return {"error": "no such user"}
        users_orders = self.db.orders.find({"client_id": ObjectId(str(user["_id"]))})
        if users_orders is None:
            return {"error": "no orders in bascket"}
        for order in users_orders:
            products = order["products"]

            for product in products:
                one_printer = self.db.printers.find_one({"_id": product["product_id"]})
                if one_printer is None:
                    continue
                bascket_counter += one_printer["price"]
        return bascket_counter
    
    def get_all_printers(self) -> dict: 
        try:
            all_printers = list(self.db.printers.find({}))
            for i in all_printers:
                i['category_id'] = str(i['category_id'])
            return {"printers": all_printers}
        except Exception as e:
            return {'error': str(e)}
        
    def add_new_printer(self, new_printer: dict) -> dict:
           try:
               new_printer['category_id'] = ObjectId(new_printer['category_id'])
               self.db.printers.insert_one(new_printer)
               return {'status': 200} 
           except Exception as e:
               return {'error': str(e)}          
               
    def delele_one_printer(self, item_id :str) -> dict:
        try:
            self.db.printers.delete_one({'_id': ObjectId(item_id)})
            return {'status': 200} 
        except Exception as e:
            return {'error': str(e)}
