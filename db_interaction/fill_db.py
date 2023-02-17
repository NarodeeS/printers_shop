from db_interaction.db import MongoCreator


if __name__ == "__main__":
    mongo = MongoCreator()
    mongo.db.categories.insert_many(
        [{"name": "Лазерный"}, {"name": "Светодиодный"}, {"name": "Струйный"}]
    )

    mongo.db.printers.insert_many(
        [
            {
                "manufacturer": "HP",
                "priner_name": "Color LaserJet 150nw",
                "paper_weight": 60,
                "colors_number": 2,
                "resolution": "600x600",
                "print_speed": 18,
                "cartridge_count": 4,
                "tray_capacity": 50,
                "paper_format": "A4",
                "category_id": mongo.db.categories.find_one(
                    {"name": "Лазерный"}["_id"]
                ),
                "amount": 100,
                "price": 37_999,
            },
            {
                "manufacturer": "Epson",
                "priner_name": "L805",
                "paper_weight": 300,
                "colors_number": 2,
                "resolution": "5760x1440",
                "print_speed": 5,
                "cartridge_count": 6,
                "tray_capacity": 120,
                "paper_format": "A4",
                "category_id": mongo.db.categories.find_one(
                    {"name": "Струйный"}["_id"]
                ),
                "amount": 100,
                "price": 31_999,
            },
        ]
    )
