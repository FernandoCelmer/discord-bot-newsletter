from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    type: str
    title: str
    link: str
    status: Optional[bool] = True


class SchemaPatch(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    status: Optional[bool] = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        from_attributes = False
