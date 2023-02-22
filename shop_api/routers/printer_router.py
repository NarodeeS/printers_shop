from fastapi import APIRouter
from pydantic.types import Json
from starlette import status
from mongo_db.mongo_client import MongoClientHandler
from schemas import CreatePrinterSchema


printer_router = APIRouter(prefix='/printers', tags=['printers'])


@printer_router.get('/')
def get_printers():
   client = MongoClientHandler()
   all_printers = client.get_all_printers()
   print(all_printers)
   print(type(all_printers))
   return all_printers


@printer_router.post('/')
def post_printers(new_printer: CreatePrinterSchema):
    client = MongoClientHandler()
    status = client.add_new_printer(new_printer.dict())
    return status
        

@printer_router.delete('/{item_id}')
def delete_printers(item_id: int):
    client = MongoClientHandler()
    all_printers = client.delele_one_printer(item_id=item_id)
    return all_printers
