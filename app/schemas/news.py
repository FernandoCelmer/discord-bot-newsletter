from datetime import date

from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    title: str
    category: str
    url: str
    thumbnail: str
    description: str
    status: bool = True
    scheduled: date = None


class SchemaPatch(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    description: Optional[str] = None
    status: bool = None
    scheduled: date = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        from_attributes = False
