from sqlmodel import Session
from jose import JWTError

from starlette.requests import Request
from sqladmin.authentication import AuthenticationBackend

from app.db import engine
from app.models.user import User
from app.interactors.auth.login import Login
from app.utils.decode_access_token import decode_access_token


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()

        with Session(engine) as session:
            response = Login.call(form["username"], form["password"], session)

            if not response["user"].is_admin:
                return False

            request.session.update({"access_token": response["access_token"]})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("access_token")

        if not token:
            return False

        try:
            payload = decode_access_token(token)
            user_id = payload.get("sub")

        except JWTError:
            return False

        with Session(engine) as session:
            user = session.get(User, user_id)

            if user is None:
                return False

            if not user.is_admin:
                return False

        return True
