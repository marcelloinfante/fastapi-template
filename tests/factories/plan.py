from uuid import UUID

from pydantic import Field
from sqlmodel import Session

from faker import Faker
from faker.providers import lorem

from app.models.plan import Plan, TypeEnum

from tests.factories.base import BaseFactory

fake = Faker()
fake.add_provider(lorem)


class PlanFactory(BaseFactory):
    user_id: UUID | None = None

    type: TypeEnum | None = TypeEnum.BASIC

    def new(self) -> Plan:
        return Plan.model_validate(self)

    def create(self, session: Session) -> Plan:
        plan = self.new()

        session.add(plan)
        session.commit()
        session.refresh(plan)

        return plan
