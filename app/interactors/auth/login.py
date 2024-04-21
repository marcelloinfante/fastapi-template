from fastapi import HTTPException, status
from sqlmodel import Session, select

from pydantic import EmailStr

from passlib.context import CryptContext

from app.models.user import User, UserSession

from app.utils.create_access_token import create_access_token


class Login:
    @classmethod
    def call(self, username: EmailStr, password: str, session: Session) -> UserSession:
        user = self._authenticate_user(username, password, session)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(user.id)

        return {"user": user, "access_token": access_token}

    @classmethod
    def _authenticate_user(
        self, username: EmailStr, password: str, session: Session
    ) -> User:
        statement = select(User).where(User.email == username)
        results = session.exec(statement)

        user = results.one_or_none()

        if not user or not password:
            return False

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        if not pwd_context.verify(password, user.hashed_password):
            return False

        return user
