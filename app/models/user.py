from datetime import datetime

from uuid import UUID, uuid4
from typing import Optional

from pydantic import EmailStr
from sqlalchemy import DateTime, func
from sqlmodel import SQLModel, AutoString, Column, Field, Relationship

from sqlalchemy import UniqueConstraint


class UserBase(SQLModel):
    email: EmailStr = Field(index=True, sa_type=AutoString)
    first_name: str
    last_name: str


class User(UserBase, table=True):
    __table_args__ = (UniqueConstraint("email"),)

    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    is_admin: bool = False
    hashed_password: str

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


class UserSession(SQLModel):
    user: UserRead
    access_token: str


class UserUpdate(SQLModel):
    first_name: str | None = None
    last_name: str | None = None
