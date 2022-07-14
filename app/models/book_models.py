from sqlalchemy import Column, Integer, SmallInteger, DateTime, String, func

from app.config.database import Base


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    coverImageUrl = Column(String(255))
    language = Column(String(50))  # TODO: might extract to another table
    country = Column(String(255))
    author = Column(String(255))
    description = Column(String(255))
    totalPages = Column(SmallInteger)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    # categories
    # lastRentalDate
    # isInStock
