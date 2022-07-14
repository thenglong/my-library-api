from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class BaseBookSchema(BaseModel):
    title: str
    language: Optional[str]
    country: Optional[str]
    coverImageUrl: Optional[str]
    author: Optional[str]
    description: Optional[str]
    totalPages: Optional[int]


class BookSchema(BaseBookSchema):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True
