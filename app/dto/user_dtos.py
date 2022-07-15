from typing import Optional, List

from pydantic import constr, EmailStr

from app.core.enums import UserRole
from app.dto.common_dtos import CamelModel


class BaseUserDto(CamelModel):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    description: Optional[str]
    phone: Optional[str]
    photo_url: Optional[str]


class CreateAdminUserDto(BaseUserDto):
    password: constr(min_length=8)


class UserResponseDto(BaseUserDto):
    id: int
    roles: List[UserRole]

    class Config:
        orm_mode = True
