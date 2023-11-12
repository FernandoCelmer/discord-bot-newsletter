from uuid import UUID, uuid4
from datetime import date
from pydantic import BaseModel, Field, field_validator


class SchemaNews(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    category: str
    url: str
    thumbnail: str
    description: str
    status: bool
    scheduled: date

    @field_validator('title')
    @classmethod
    def validate_title(cls, value: str) -> str:
        return value.rjust(75)

    @field_validator('description')
    @classmethod
    def validate_description(cls, value: str) -> str:
        return f'{value}...'


class SchemaChannel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    code: str
    status: bool
