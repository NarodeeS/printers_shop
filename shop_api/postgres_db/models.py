from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, SmallInteger
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Worker(Base):
    __tablename__ = 'workers'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    login = Column(String(50) , nullable=False)
    mobile_number = Column(BigInteger, nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    position_code = Column(SmallInteger, ForeignKey('position_classifiers.code'))


class PositionClassifier(Base):
    __tablename__ = 'position_classifiers'
    
    code = Column(SmallInteger, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String(50), nullable=False)
