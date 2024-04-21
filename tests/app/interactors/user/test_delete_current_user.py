import pytest

from sqlmodel import Session
from fastapi import HTTPException

from app.models.user import User
from app.interactors.user.delete_current_user import DeleteCurrentUser

from tests.factories.user import UserFactory


def test_delete_current_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    DeleteCurrentUser.call(session=session, current_user=user)

    result = session.get(User, user.id)

    assert result == None


def test_delete_current_user_without_user(session: Session):
    with pytest.raises(HTTPException) as e:
        DeleteCurrentUser.call(session=session, current_user=None)

    assert "400: Data invalid" == str(e.value)
