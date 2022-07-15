from sqlalchemy import Column, DateTime, func, Integer, Boolean

from app.core.database import Base


class Audit(Base):
    __abstract__ = True
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    is_archived = Column(Boolean, nullable=False, default=False)
    deleted_by = Column(Integer)
