from fastapi import APIRouter, Depends

from sqlmodel import Session

from app.models.user import User, UserRead, UserUpdate

from app.dependencies.get_session import get_session
from app.dependencies.get_current_user import get_current_user

from app.interactors.user.update_current_user import UpdateCurrentUser
from app.interactors.user.delete_current_user import DeleteCurrentUser


router = APIRouter(prefix="/user", tags=["user"])


@router.get("", response_model=UserRead, status_code=200)
def get_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("", response_model=UserRead, status_code=200)
def update_current_user(
    user: UserUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    response = UpdateCurrentUser.call(user, session, current_user)

    return response


@router.delete("", status_code=200)
def delete_current_user(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    DeleteCurrentUser.call(session, current_user)
