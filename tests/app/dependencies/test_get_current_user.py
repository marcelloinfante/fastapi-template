import pytest

from datetime import datetime, timedelta

from fastapi.exceptions import HTTPException

from jose import jwt

from app.dependencies.get_current_user import get_current_user
from app.utils.create_access_token import create_access_token

from app.models.user import User

from tests.factories.user import UserFactory

from app.config import settings


def test_get_current_user(session):
    created_user = UserFactory().create(session)

    token = create_access_token(created_user.id)

    user = get_current_user(session, token)

    assert User(**user.model_dump())


def test_get_current_user_with_expired_token(session):
    created_user = UserFactory().create(session)

    expire = datetime.utcnow() - timedelta(minutes=10)

    to_encode = {"sub": str(created_user.id), "exp": expire}

    token = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.hash_algorithm
    )

    with pytest.raises(HTTPException):
        get_current_user(session, token)


def test_get_current_user_with_invalid_token(session):
    with pytest.raises(HTTPException):
        get_current_user(session, "invalid_token")


def test_get_current_user_with_invalid_user(session):
    created_user = UserFactory().create(session)

    token = create_access_token(created_user.id)

    session.delete(created_user)
    session.commit()

    with pytest.raises(HTTPException):
        get_current_user(session, token)


def test_get_current_user_without_user_id(session):
    token = create_access_token("4620d19b-f086-4fdd-a4c3-f1daa2a99317")

    with pytest.raises(HTTPException):
        get_current_user(session, token)
