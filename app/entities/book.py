from sqlalchemy import Column, Integer, SmallInteger, String, Sequence

from app.entities.common import Audit


class Book(Audit):
    __tablename__ = "books"

    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    title = Column(String(255), nullable=False)
    cover_image_url = Column(String(255))
    language = Column(String(50))  # TODO: might extract to another table
    country = Column(String(255))
    author = Column(String(255))
    publisher = Column(String(255))
    edition = Column(String(255))
    description = Column(String(255))
    page_count = Column(SmallInteger)
    # rent_count = Column(Integer)
    # categories
    # lastRentalDate
    # isInStock
