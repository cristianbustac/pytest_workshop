

from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    POSTGRES_DATABASE_URL: str = Field(...)

