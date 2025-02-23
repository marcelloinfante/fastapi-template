from sqlmodel import Session

from app.models.plan import Plan
from app.models.user import User, UserIn, UserSession

from app.utils.encrypt_password import encrypt_password
from app.utils.create_access_token import create_access_token
from app.decorators.handle_http_exception import handle_http_exception


class Register:
    @classmethod
    @handle_http_exception
    def call(cls, user: UserIn, session: Session) -> UserSession:
        hashed_password = encrypt_password(user.password)

        user = user.model_dump(exclude={"password"})
        user.update({"hashed_password": hashed_password})

        user = User.model_validate(user)
        plan = Plan(user=user)

        session.add_all([user, plan])
        session.commit()
        session.refresh(user)

        access_token = create_access_token(user.id)

        return {"user": user, "access_token": access_token}
