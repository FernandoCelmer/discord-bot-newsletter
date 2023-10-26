from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    name: Optional[str]
    status: Optional[bool] = True


class SchemaPatch(BaseModel):
    name: Optional[str] = None
    status: Optional[bool] = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        from_attributes = False