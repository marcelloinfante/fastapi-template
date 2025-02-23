from enum import Enum
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class EnvironmentEnum(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


class Settings(BaseSettings):
    secret_key: str = "123456789"
    allow_origin: str = "*"
    environment: EnvironmentEnum = EnvironmentEnum.DEVELOPMENT
    database_url: str = "postgresql://fastapi:fastapi@db:5432/fastapi"
    hash_algorithm: str = "HS256"
    admin_secret_key: str = "360"
    access_token_expire_minutes: int = 360


settings = Settings()
