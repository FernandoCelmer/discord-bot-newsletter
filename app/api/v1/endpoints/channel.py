from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Request, status

from app.core.database import get_db
from app.schemas.channel import Schema, SchemaPatch
from app.controllers.channel import ControllerChannel as Controller


router = APIRouter()


@router.get("/channel", response_model=List[Schema])
def get_all(
        request: Request,
        offset: int = 0,
        limit: int = 100,
        sort_by: str = 'id',
        order_by: str = 'desc',
        db: Session = Depends(get_db)):
    return Controller(db=db).read(
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        order_by=order_by,
        qtype='all',
        params=request.query_params._dict
    )


@router.get("/channel/{id}", response_model=Schema)
def get_one(id: int, db: Session = Depends(get_db)):
    return Controller(db=db).read(
        qtype='first',
        params={"id": id}
    )


@router.patch("/channel/{model_id}", response_model=Schema)
def update(model_id: int, item: SchemaPatch, db: Session = Depends(get_db)):
    return Controller(db=db).update(data=item.dict(), model_id=model_id)


@router.post("/channel/", response_model=Schema, status_code=status.HTTP_201_CREATED)
def create(item: Schema, db: Session = Depends(get_db)):
    return Controller(db=db).create(data=item.dict())
