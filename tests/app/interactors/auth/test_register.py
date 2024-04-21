import pytest

from sqlmodel import Session
from fastapi import HTTPException

from app.models.user import User, UserIn

from app.interactors.auth.register import Register

from tests.factories.user import UserFactory


def test_register(session: Session):
    user_factory = UserFactory()
    user = UserIn.model_validate(user_factory)

    result = Register.call(user=user, session=session)
    user = session.get(User, result["user"].id)

    assert result["user"] == user
    assert isinstance(result["user"], User)
    assert isinstance(result["access_token"], str)


def test_register_without_user_email(session: Session):
    user_factory = UserFactory(email=None)

    with pytest.raises(HTTPException) as e:
        Register.call(user=user_factory, session=session)

    assert "400: Data invalid" == str(e.value)


def test_register_without_user_first_name(session: Session):
    user_factory = UserFactory(first_name=None)

    with pytest.raises(HTTPException) as e:
        Register.call(user=user_factory, session=session)

    assert "400: Data invalid" == str(e.value)


def test_register_without_user_last_name(session: Session):
    user_factory = UserFactory(last_name=None)

    with pytest.raises(HTTPException) as e:
        Register.call(user=user_factory, session=session)

    assert "400: Data invalid" == str(e.value)


def test_register_without_user_password(session: Session):
    user_factory = UserFactory(password=None)

    with pytest.raises(HTTPException) as e:
        Register.call(user=user_factory, session=session)

    assert "400: Data invalid" == str(e.value)
