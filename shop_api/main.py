from postgres_db.models import Base
from postgres_db.base import engine
from postgres_db.utils import wait_unlesss_db_started
from postgres_db.init_classifiers import init_classifiers
from mongo_db.init_mongo import init_categories
from mongo_db.create_db import create_db

from api import get_app


app = get_app()
wait_unlesss_db_started()
Base.metadata.create_all(bind=engine)

create_db()
init_classifiers()
init_categories()

