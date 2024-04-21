import pytest

from sqlmodel import Session
from fastapi import HTTPException

from app.models.user import User, UserUpdate
from app.interactors.user.update_current_user import UpdateCurrentUser

from tests.factories.user import UserFactory


def test_update_current_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    user_update_factory = UserFactory(
        first_name="ALKDSJFIOAJER", last_name="KSJIRRRTBGDF"
    )
    user_update = UserUpdate.model_validate(user_update_factory)

    result = UpdateCurrentUser.call(
        user=user_update, session=session, current_user=user
    )

    assert isinstance(result, User)

    assert result.id == user.id
    assert result.email == user.email
    assert result.last_name == user_update.last_name
    assert result.first_name == user_update.first_name

    assert user_factory.last_name != user_update.last_name
    assert user_factory.first_name != user_update.first_name


def test_update_current_user_without_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    with pytest.raises(HTTPException) as e:
        UpdateCurrentUser.call(user=None, session=session, current_user=user)

    assert "400: Data invalid" == str(e.value)


def test_update_current_user_without_user(session: Session):
    user_factory = UserFactory()

    with pytest.raises(HTTPException) as e:
        UpdateCurrentUser.call(user=user_factory, session=session, current_user=None)

    assert "400: Data invalid" == str(e.value)
