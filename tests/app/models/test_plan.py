from uuid import UUID
from datetime import datetime

import pytest
from sqlmodel import Session
from pydantic_core._pydantic_core import ValidationError


from app.models.plan import Plan, TypeEnum
from tests.factories.plan import PlanFactory
from tests.factories.user import UserFactory


def test_create_plan(session: Session):
    plan_factory = PlanFactory()
    plan = plan_factory.create(session)

    assert isinstance(plan, Plan)
    assert isinstance(plan.id, UUID)
    assert isinstance(plan.type, TypeEnum)
    assert isinstance(plan.created_at, datetime)
    assert isinstance(plan.updated_at, datetime)

    assert plan.type == plan_factory.type


def test_create_plan_with_user(session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan = plan_factory.create(session)

    assert user.plan == plan
    assert plan.user == user


def test_create_plan_without_type(session: Session):
    plan_factory = PlanFactory(type=None)

    with pytest.raises(ValidationError) as e:
        plan_factory.create(session)

    assert "Input should be 'BASIC', 'STARTER' or 'PREMIUM'" in str(e.value)


def test_update_plan(session: Session):
    plan_factory = PlanFactory()
    plan = plan_factory.create(session)

    plan.type = TypeEnum.PREMIUM

    session.add(plan)
    session.commit()
    session.refresh(plan)

    assert plan.type == TypeEnum.PREMIUM
    assert plan.created_at < plan.updated_at
