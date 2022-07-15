from fastapi import HTTPException, status
from firebase_admin import auth
from sqlalchemy.orm import Session

from app.core.enums import UserRole
from app.dto.user_dtos import CreateAdminUserDto
from app.entities.user import User


def create_admin(request: CreateAdminUserDto, db: Session):
    try:
        firebase_user = auth.create_user(
            email=request.email,
            email_verified=False,  # TODO
            # phone_number=request.phone, # TODO: Phone number need to be validate or google will throw error
            password=request.password,
            display_name=f"{request.first_name} {request.last_name}",
            photo_url=request.photo_url,
            disabled=False)
        auth.set_custom_user_claims(firebase_user.uid, {"roles": [UserRole.ADMIN]})

        new_user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            description=request.description,
            phone=request.phone,
            photo_url=request.photo_url,
            roles=[UserRole.ADMIN]
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error Occurs",
        )
