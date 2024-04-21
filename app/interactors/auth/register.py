from fastapi import HTTPException, status
from sqlmodel import Session

from app.models.user import User, UserIn, UserSession

from app.utils.encrypt_password import encrypt_password
from app.utils.create_access_token import create_access_token


class Register:
    @classmethod
    def call(self, user: UserIn, session: Session) -> UserSession:
        try:
            hashed_password = encrypt_password(user.password)

            user = user.model_dump(exclude={"password"})
            user.update({"hashed_password": hashed_password})

            user = User.model_validate(user)

            session.add(user)
            session.commit()
            session.refresh(user)

            access_token = create_access_token(user.id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Data invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {"user": user, "access_token": access_token}
