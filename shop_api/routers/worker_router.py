from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from postgres_db.get_session import get_session
from postgres_db.models import Worker
from schemas import CreateWorkerSchema, ReturnWorkerSchema


worker_router = APIRouter(prefix='/workers', tags=['workers'])


@worker_router.get('/', response_model=list[ReturnWorkerSchema])
def get_workers(postgres_session: Session = Depends(get_session)):
    return postgres_session.query(Worker).all()


@worker_router.post('/', response_model=ReturnWorkerSchema)
def create_worker(new_worker: CreateWorkerSchema,
                  postgres_session: Session = Depends(get_session)):
    worker = Worker(**new_worker.dict())
    postgres_session.add(worker)
    postgres_session.commit()
    postgres_session.refresh(worker)
    return worker


@worker_router.delete('/{id:int}', status_code=200)
def delete_worker(id: int,
                  postgres_session: Session = Depends(get_session)):
    candidate = postgres_session.query(Worker).get(id)
    if candidate is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='No user with such id')
    postgres_session.delete(candidate)
    postgres_session.commit()
    return {'message': 'Deleted successfully'}
