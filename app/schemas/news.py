from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    type: str
    title: str
    link: str
    status: Optional[bool] = True


class SchemaPatch(BaseModel):
    type: Optional[bool]
    title: Optional[bool]
    link: Optional[bool]
    status: Optional[bool]


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        from_attributes = False
