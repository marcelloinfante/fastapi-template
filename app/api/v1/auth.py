from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlmodel import Session

from app.models.user import UserIn, UserSession

from app.interactors.auth.login import Login
from app.interactors.auth.register import Register

from app.dependencies.get_session import get_session


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserSession)
def login(
    session: Session = Depends(get_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    response = Login.call(form_data.username, form_data.password, session)

    return response


@router.post("/register", response_model=UserSession, status_code=201)
def register(
    user: UserIn,
    session: Session = Depends(get_session),
):
    response = Register.call(user, session)

    return response
