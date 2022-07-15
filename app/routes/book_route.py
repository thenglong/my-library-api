from typing import Union

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dto.book_dtos import BookResponseDto, BaseBookDto
from app.dto.common_dtos import Pagination
from app.services import book_service

router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@router.get("", response_model=Pagination[BookResponseDto])
def get_paginated_book(page: Union[int, None] = Query(default=1,ge=1),
                       take: Union[int, None] = Query(default=20),
                       db: Session = Depends(get_db)):
    return book_service.get_all(page=page, take=take, db=db)


@router.post("", response_model=BookResponseDto, status_code=status.HTTP_201_CREATED)
def create_book(request: BaseBookDto,

                db: Session = Depends(get_db)):
    return book_service.create(request=request, db=db)


@router.get("/{book_id}", response_model=BookResponseDto)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_by_id(book_id=book_id, db=db)


@router.put("/{book_id}", response_model=BookResponseDto)
def update_book(book_id: int, request: BaseBookDto,
                db: Session = Depends(get_db)):
    return book_service.update(book_id=book_id, request=request, db=db)


@router.delete("/{book_id}", response_model=bool)
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.delete(book_id=book_id, db=db)
