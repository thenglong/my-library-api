from fastapi import Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth

from app.core.enums import UserRole


class UserAuthorizer:
    def __init__(self, *roles: UserRole):
        self.roles = roles

    def __call__(self, response: Response,
                 credential: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
        if credential is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Bearer authentication is needed",
                headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
            )
        try:
            decoded_token = auth.verify_id_token(credential.credentials, check_revoked=True)
            authorized = False
            for role in UserRole:
                if role in decoded_token['roles']:
                    authorized = True
                    break
            if not authorized:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Unauthorized resource",
                )
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid authentication from Firebase. {err}",
                headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
            )
        response.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
        return decoded_token
