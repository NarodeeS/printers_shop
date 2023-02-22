from fastapi import FastAPI

from routers.printer_router import printer_router
from routers.worker_router import worker_router
from postgres_db.models import Base
from postgres_db.base import engine
from postgres_db.utils import wait_unlesss_db_started


wait_unlesss_db_started()
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(printer_router)
app.include_router(worker_router)

@app.get('/')
def home():
    return {'message': 'OK'}
