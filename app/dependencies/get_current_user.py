from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlmodel import Session

from jose import JWTError

from app.models.user import User

from app.dependencies.get_session import get_session
from app.utils.decode_access_token import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

    except JWTError:
        raise credentials_exception

    user = session.get(User, user_id)

    if user is None:
        raise credentials_exception

    return user
