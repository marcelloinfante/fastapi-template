from fastapi import HTTPException, status

from sqlmodel import Session

from app.models.user import User, UserUpdate


class UpdateCurrentUser:
    @classmethod
    def call(self, user: UserUpdate, session: Session, current_user: User) -> User:
        try:
            user_data = user.model_dump(exclude_unset=True)

            for key, value in user_data.items():
                setattr(current_user, key, value)

            session.add(current_user)
            session.commit()
            session.refresh(current_user)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Data invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return current_user
