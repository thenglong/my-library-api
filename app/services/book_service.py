from fastapi import HTTPException
from sqlalchemy import desc, asc, or_
from sqlalchemy.orm.session import Session

from app.dto.book_dtos import BaseBookDto
from app.dto.common_dtos import PaginateQueryParams, PaginateWithSearchQueryParams
from app.entities.book import Book
from app.helpers.response import create_pagination_from_paginate_params


def get_all(paginate_request: PaginateWithSearchQueryParams, db: Session):
    page = paginate_request.page
    take = paginate_request.take
    search = paginate_request.get_search_query()
    offset = paginate_request.get_offset()

    query = db.query(Book)

    result = query \
        .order_by(desc(Book.title)) \
        .order_by(asc(Book.id)) \
        .offset(offset) \
        .limit(take) \
        .all()
    all_book_count = query.count()
    return create_pagination_from_paginate_params(items=result,
                                                  paginate=paginate_request,
                                                  all_items_count=all_book_count)


def create(request: BaseBookDto, db: Session):
    new_book = Book(
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
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    return book


def update(book_id: int, request: BaseBookDto, db: Session):
    book = db.query(Book).get(book_id)
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
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    db.delete(book)
    db.commit()
    return True
