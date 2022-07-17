import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column, Integer, Sequence, String, CheckConstraint

from app.core.enums import UserRole
from app.entities.common import Audit


class User(Audit):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("roles <> '{}'", name='roles_not_empty'),
    )

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), nullable=False)
    description = Column(String(255))
    phone = Column(String(50))
    photo_url = Column(String(255))
    roles = Column(pg.ARRAY(pg.ENUM(UserRole, name="user_role_enum")), nullable=False)
