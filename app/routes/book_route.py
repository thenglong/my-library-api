from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.dto.book_schema import BookSchema, BaseBookSchema
from app.config.database import get_db
from app.dto.common_schema import Pagination
from typing import Union
from app.services import book_service

router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@router.get("/", response_model=Pagination[BookSchema])
def get_all(page: Union[int, None] = Query(default=1),
            take: Union[int, None] = Query(default=20),
            db: Session = Depends(get_db)):
    return book_service.get_all(page=page, take=take, db=db)


@router.post("/", response_model=BookSchema)
def create(request: BaseBookSchema, db: Session = Depends(get_db)):
    return book_service.create(request=request, db=db)


@router.get("/{book_id}", response_model=BookSchema)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_by_id(book_id=book_id, db=db)


@router.put("/{book_id}", response_model=BookSchema)
def update(book_id: int, request: BaseBookSchema,
           db: Session = Depends(get_db)):
    return book_service.update(book_id=book_id, request=request, db=db)


@router.delete("/{book_id}", response_model=bool)
def delete(book_id: int, db: Session = Depends(get_db)):
    return book_service.delete(book_id=book_id, db=db)
