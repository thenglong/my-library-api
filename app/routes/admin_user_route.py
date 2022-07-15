from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.auth import UserAuthorizer
from app.core.database import get_db
from app.core.enums import UserRole
from app.dto.user_dtos import UserResponseDto, CreateAdminUserDto
from app.services import user_service

router = APIRouter(prefix="/api/v1/users/admin", tags=["Admin Users"])


@router.post("", response_model=UserResponseDto, status_code=status.HTTP_201_CREATED)
def create_admin(request: CreateAdminUserDto,
                 decoded_token=Depends(UserAuthorizer(UserRole.ADMIN)),
                 db: Session = Depends(get_db)):
    print(decoded_token['roles'])
    return user_service.create_admin(request=request, db=db)


