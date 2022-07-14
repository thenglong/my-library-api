from typing import Optional

from pydantic import BaseModel, Field


class BaseBookDto(BaseModel):
    title: str
    language: Optional[str]
    country: Optional[str]
    cover_image_url: Optional[str] = Field(..., alias="coverImageUrl")
    author: Optional[str]
    description: Optional[str]
    page_count: Optional[int] = Field(..., alias="pageCount")

    class Config:
        allow_population_by_field_name = True


class BookDto(BaseBookDto):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
