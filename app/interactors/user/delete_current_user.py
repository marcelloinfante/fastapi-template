from sqlmodel import Session

from app.models.user import User
from app.decorators.handle_http_exception import handle_http_exception


class DeleteCurrentUser:
    @classmethod
    @handle_http_exception
    def call(cls, session: Session, current_user: User) -> None:
        session.delete(current_user)
        session.commit()
