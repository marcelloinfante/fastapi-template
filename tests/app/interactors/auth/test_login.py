import pytest

from sqlmodel import Session
from fastapi import HTTPException

from app.models.user import User
from app.interactors.auth.login import Login

from tests.factories.user import UserFactory


def test_login(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    result = Login.call(
        username=user_factory.email, password=user_factory.password, session=session
    )

    assert result["user"] == user
    assert isinstance(result["user"], User)
    assert isinstance(result["access_token"], str)


def test_login_without_username(session: Session):
    user_factory = UserFactory()
    user_factory.create(session)

    with pytest.raises(HTTPException) as e:
        Login.call(username=None, password=user_factory.password, session=session)

    assert "401: Incorrect username or password" == str(e.value)


def test_login_without_password(session: Session):
    user_factory = UserFactory()
    user_factory.create(session)

    with pytest.raises(HTTPException) as e:
        Login.call(username=user_factory.email, password=None, session=session)

    assert "401: Incorrect username or password" == str(e.value)


def test_login_with_wrong_username(session: Session):
    user_factory = UserFactory()
    user_factory.create(session)

    with pytest.raises(HTTPException) as e:
        Login.call(username="12345", password=user_factory.password, session=session)

    assert "401: Incorrect username or password" == str(e.value)


def test_login_with_wrong_password(session: Session):
    user_factory = UserFactory()
    user_factory.create(session)

    with pytest.raises(HTTPException) as e:
        Login.call(username=user_factory.email, password="12345", session=session)

    assert "401: Incorrect username or password" == str(e.value)
