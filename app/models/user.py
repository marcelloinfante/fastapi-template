from datetime import datetime

from uuid import UUID, uuid4
from typing import Optional

from pydantic import EmailStr
from sqlmodel import AutoString, Column, Field, Relationship
from sqlalchemy import UniqueConstraint, DateTime, func

from app.models.base import BaseSQLModel


class UserBase(BaseSQLModel):
    email: EmailStr = Field(index=True, sa_type=AutoString)
    first_name: str
    last_name: str


class User(UserBase, table=True):
    __table_args__ = (UniqueConstraint("email"),)

    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    is_admin: bool = False
    hashed_password: str

    plan: Optional["Plan"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="user"
    )

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


class UserIn(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID

    created_at: datetime
    updated_at: datetime

    plan: "PlanRead"


class UserSession(BaseSQLModel):
    user: UserRead
    access_token: str


class UserUpdate(BaseSQLModel):
    first_name: str | None = None
    last_name: str | None = None


from app.models.plan import Plan, PlanRead

UserBase.model_rebuild()
User.model_rebuild()
UserIn.model_rebuild()
UserRead.model_rebuild()
UserSession.model_rebuild()
UserUpdate.model_rebuild()
