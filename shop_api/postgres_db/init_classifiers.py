from .base import SessionLocal
from .models import PositionClassifier


def init_classifiers():
    session = SessionLocal()
    classifiers = session.query(PositionClassifier).all()
    if len(classifiers) == 0:
        session.add(PositionClassifier(description='admin'))
        session.add(PositionClassifier(description='manager'))
        session.add(PositionClassifier(description='worker'))
        session.commit()
