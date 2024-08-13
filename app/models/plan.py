from datetime import datetime

from enum import Enum
from uuid import UUID, uuid4
from typing import Optional

from sqlalchemy import DateTime, func
from sqlmodel import Column, Field, Relationship

from app.models.base import BaseSQLModel


class TypeEnum(str, Enum):
    BASIC = "BASIC"
    STARTER = "STARTER"
    PREMIUM = "PREMIUM"


class PlanBase(BaseSQLModel):
    type: TypeEnum = TypeEnum.BASIC


class Plan(PlanBase, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)

    user_id: UUID | None = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="plan")

    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )

    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=True,
        ),
    )


class PlanRead(PlanBase):
    created_at: datetime
    updated_at: datetime


from app.models.user import User

PlanBase.model_rebuild()
Plan.model_rebuild()
PlanRead.model_rebuild()
