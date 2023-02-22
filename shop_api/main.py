from postgres_db.models import Base
from postgres_db.base import engine
from postgres_db.utils import wait_unlesss_db_started
from postgres_db.init_classifiers import init_classifiers
from mongo_db.init_mongo import init_categories
from api import app


wait_unlesss_db_started()
Base.metadata.create_all(bind=engine)
init_classifiers()
init_categories()
