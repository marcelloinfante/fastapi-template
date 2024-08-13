from uuid import UUID
from datetime import datetime

import pytest
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User

from tests.factories.user import UserFactory
from tests.factories.plan import PlanFactory


def test_create_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    assert isinstance(user, User)
    assert isinstance(user.id, UUID)
    assert isinstance(user.email, str)
    assert isinstance(user.first_name, str)
    assert isinstance(user.last_name, str)
    assert isinstance(user.is_admin, bool)
    assert isinstance(user.hashed_password, str)
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.updated_at, datetime)

    assert user.email == user_factory.email
    assert user.first_name == user_factory.first_name
    assert user.last_name == user_factory.last_name
    assert user.is_admin == user_factory.is_admin


def test_create_user_with_plan(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan = plan_factory.create(session)

    assert user.plan == plan
    assert plan.user == user


def test_create_user_without_email(session: Session):
    user_factory = UserFactory(email=None)

    with pytest.raises(IntegrityError) as e:
        user_factory.create(session)

    assert (
        'null value in column "email" of relation "user" violates not-null constraint'
        in str(e.value)
    )


def test_create_user_without_first_name(session: Session):
    user_factory = UserFactory(first_name=None)

    with pytest.raises(IntegrityError) as e:
        user_factory.create(session)

    assert (
        'null value in column "first_name" of relation "user" violates not-null constraint'
        in str(e.value)
    )


def test_create_user_without_last_name(session: Session):
    user_factory = UserFactory(last_name=None)

    with pytest.raises(IntegrityError) as e:
        user_factory.create(session)

    assert (
        'null value in column "last_name" of relation "user" violates not-null constraint'
        in str(e.value)
    )


def test_update_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    user.email = "example@example.com"
    user.first_name = "First"
    user.last_name = "Last"
    user.is_admin = True

    session.add(user)
    session.commit()
    session.refresh(user)

    assert user.email == "example@example.com"
    assert user.first_name == "First"
    assert user.last_name == "Last"
    assert user.is_admin == True
    assert user.created_at < user.updated_at
