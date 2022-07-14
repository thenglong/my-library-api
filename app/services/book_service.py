from fastapi import HTTPException
from sqlalchemy import desc, asc
from sqlalchemy.orm.session import Session

from app.dto.book_dtos import BaseBookDto
from app.dto.common_dtos import create_pagination
from app.models.book_models import BookModel


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
    return create_pagination(items=result,
                             page=page,
                             all_items_count=all_book_count,
                             take=take)


def create(request: BaseBookDto, db: Session):
    new_book = BookModel(
        title=request.title,
        language=request.language,
        country=request.country,
        page_count=request.page_count,
        description=request.description,
        cover_image_url=request.cover_image_url,
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


def update(book_id: int, request: BaseBookDto, db: Session):
    book = db.query(BookModel).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    book.title = request.title
    book.language = request.language
    book.country = request.country
    book.cover_image_url = request.cover_image_url
    book.author = request.author
    book.description = request.description
    book.page_count = request.page_count

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
