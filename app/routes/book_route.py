from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.auth import get_user_token
from app.dto.book_dtos import BookDto, BaseBookDto
from app.core.database import get_db
from app.dto.common_dtos import Pagination
from typing import Union
from app.services import book_service

router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@router.get("", response_model=Pagination[BookDto])
def get_all(page: Union[int, None] = Query(default=1),
            take: Union[int, None] = Query(default=20),
            db: Session = Depends(get_db)):
    return book_service.get_all(page=page, take=take, db=db)


@router.post("", response_model=BookDto)
def create(request: BaseBookDto, db: Session = Depends(get_db)):
    return book_service.create(request=request, db=db)


@router.get("/{book_id}", response_model=BookDto)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_by_id(book_id=book_id, db=db)


@router.put("/{book_id}", response_model=BookDto)
def update(book_id: int, request: BaseBookDto,
           db: Session = Depends(get_db),
           user=Depends(get_user_token)):
    return book_service.update(book_id=book_id, request=request, db=db)


@router.delete("/{book_id}", response_model=bool)
def delete(book_id: int, db: Session = Depends(get_db)):
    return book_service.delete(book_id=book_id, db=db)
