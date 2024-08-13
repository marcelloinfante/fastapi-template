import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from sqlmodel import Session
from app.db import engine

from tests.factories.user import UserFactory
from tests.factories.plan import PlanFactory


with Session(engine) as session:
    user_admin = UserFactory(
        email="test@test.com", password="test123", is_admin=True
    ).create(session=session)

    plan = PlanFactory(user_id=user_admin.id).create(session)
