from uuid import UUID, uuid4

from typing import Optional
from pydantic import BaseModel, Field


class SchemaBase(BaseModel):
    name: str
    code: str
    status: bool = True


class SchemaPatch(BaseModel):
    name: str = None
    code: str = None
    status: bool = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: UUID = Field(default_factory=uuid4)

    class Config:
        from_attributes = False
