from fastapi import APIRouter

from mongo_db.mongo_client import MongoClientHandler
import schemas


category_router = APIRouter(prefix='/categories', tags=["categories"])


@category_router.get('/', 
                     response_model=list[schemas.ReturnCategorySchema])
def get_categories():
    client = MongoClientHandler()
    return client.get_all_categories()
