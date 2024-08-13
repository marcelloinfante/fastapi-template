from pydantic import EmailStr, Field
from sqlmodel import Session

from faker import Faker

from app.models.user import User

from app.utils.encrypt_password import encrypt_password

from tests.factories.base import BaseFactory

fake = Faker()


class UserFactory(BaseFactory):
    is_admin: bool | None = False

    email: EmailStr | None = Field(default_factory=fake.unique.email)
    password: str | None = Field(default_factory=fake.password)
    last_name: str | None = Field(default_factory=fake.unique.last_name)
    first_name: str | None = Field(default_factory=fake.unique.first_name)

    def new(self) -> User:
        hashed_password = encrypt_password(self.password)

        user = self.model_dump(exclude={"password"})
        user.update({"hashed_password": hashed_password})

        return User(**user)

    def create(self, session: Session) -> User:
        user = self.new()

        session.add(user)
        session.commit()
        session.refresh(user)

        return user
