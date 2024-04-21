from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    secret_key: str
    environment: str
    allow_origin: str
    database_url: str
    hash_algorithm: str
    admin_secret_key: str
    access_token_expire_minutes: int


settings = Settings()
