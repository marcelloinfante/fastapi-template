from sqlmodel import Session

from app.models.user import User, UserUpdate
from app.decorators.handle_http_exception import handle_http_exception


class UpdateCurrentUser:
    @classmethod
    @handle_http_exception
    def call(cls, user: UserUpdate, session: Session, current_user: User) -> User:
        user_data = user.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(current_user, key, value)

        session.add(current_user)
        session.commit()
        session.refresh(current_user)

        return current_user
