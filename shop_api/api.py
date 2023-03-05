from fastapi import FastAPI

from routers.printer_router import printer_router
from routers.worker_router import worker_router
from routers.category_router import category_router


tags = [
    {
        'name': 'workers',
        'description': 'Operations with workers'
    },
    {
        'name': "printers",
        'description': 'Operations with printers'
    },
    {
        'name': 'categories',
        'description': 'Operations with categories'
    }
]

app = FastAPI(title='Printers shop API', openapi_tags=tags)
app.include_router(printer_router, prefix='/api')
app.include_router(worker_router, prefix='/api')
app.include_router(category_router, prefix='/api')


def get_app():
    return app
