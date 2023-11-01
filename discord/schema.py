from datetime import date
from pydantic import BaseModel, field_validator


class SchemaNews(BaseModel):
    id: int
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
    
    class Config:
        from_attributes = False
