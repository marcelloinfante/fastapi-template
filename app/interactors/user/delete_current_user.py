from fastapi import HTTPException, status

from sqlmodel import Session

from app.models.user import User


class DeleteCurrentUser:
    @classmethod
    def call(self, session: Session, current_user: User) -> None:
        try:
            session.delete(current_user)
            session.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Data invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return
