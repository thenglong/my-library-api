from typing import Optional

from app.dto.common_dtos import CamelModel


class BaseBookDto(CamelModel):
    title: str
    language: Optional[str]
    country: Optional[str]
    cover_image_url: Optional[str]
    author: Optional[str]
    description: Optional[str]
    page_count: Optional[int]


class BookResponseDto(BaseBookDto):
    id: int

    class Config:
        orm_mode = True
