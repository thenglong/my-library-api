from fastapi import HTTPException
from sqlalchemy import desc, asc
from sqlalchemy.orm.session import Session

from app.dto.book_schema import BookSchema, BaseBookSchema
from app.dto.common_schema import Pagination
from app.models.book_models import BookModel

import math


def get_all(page: int, take: int, db: Session):
    offset = (page - 1) * take
    query = db.query(BookModel)
    result = query \
        .order_by(desc(BookModel.title)) \
        .order_by(asc(BookModel.id)) \
        .offset(offset) \
        .limit(take) \
        .all()
    all_book_count = query.count()
    page_count = math.ceil(all_book_count / take)

    return Pagination[BookSchema](
        page=page,
        items=result,
        pageCount=page_count,
        itemCount=all_book_count,
        taken=take,
        hasNext=page < all_book_count,
        hasPrevious=page > 1
    )


def create(request: BaseBookSchema, db: Session):
    new_book = BookModel(
        title=request.title,
        language=request.language,
        country=request.country,
        totalPages=request.totalPages,
        description=request.description,
        coverImageUrl=request.coverImageUrl,
        author=request.author,
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def get_by_id(book_id: int, db: Session):
    book = db.query(BookModel).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    return book


def update(book_id: int, request: BaseBookSchema, db: Session):
    book = db.query(BookModel).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    book.title = request.title
    book.language = request.language
    book.country = request.country
    book.coverImageUrl = request.coverImageUrl
    book.author = request.author
    book.description = request.description
    book.totalPages = request.totalPages

    db.commit()
    db.refresh(book)
    return book


def delete(book_id: int, db: Session):
    book = db.query(BookModel).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    db.delete(book)
    db.commit()
    return True
