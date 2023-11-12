from uuid import UUID
from typing import List
from datetime import datetime, date

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Request, status

from app.core.database import get_db
from app.schemas.news import Schema, SchemaCreate, SchemaPatch
from app.controllers.news import ControllerChannel as Controller


router = APIRouter()


@router.get("/news", response_model=List[Schema])
def get_all(
        request: Request,
        scheduled: str,
        offset: int = 0,
        limit: int = 100,
        sort_by: str = 'id',
        order_by: str = 'desc',
        db: Session = Depends(get_db)):
    scheduled = request.query_params.get("scheduled")
    if datetime.strptime(scheduled, "%Y-%m-%d").date() > date.today():
        return []

    return Controller(db=db).read(
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        order_by=order_by,
        qtype='all',
        params=request.query_params._dict
    )


@router.get("/news/{id}", response_model=Schema)
def get_one(id: UUID, db: Session = Depends(get_db)):
    return Controller(db=db).read(
        qtype='first',
        params={"id": id}
    )


@router.patch("/news/{id}", response_model=Schema)
def update(id: UUID, item: SchemaPatch, db: Session = Depends(get_db)):
    return Controller(db=db).update(data=item.dict(), id=id)


@router.post("/news", response_model=Schema, status_code=status.HTTP_201_CREATED)
def create(item: SchemaCreate, db: Session = Depends(get_db)):
    instance = Controller(db=db).create(data=item.dict())
    if not instance:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT
        )
    return instance
