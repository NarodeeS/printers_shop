from fastapi import FastAPI

from routers.printer_router import printer_router
from routers.worker_router import worker_router


tags = [
    {
        'name': 'workers',
        'description': 'Operation with workers'
    },
    {
        'name': "printers",
        'description': 'Operation with printers'
    }
]

app = FastAPI(openapi_tags=tags)
app.include_router(printer_router)
app.include_router(worker_router)


@app.get('/')
def home():
    return {'message': 'OK'}


def get_app():
    return app
