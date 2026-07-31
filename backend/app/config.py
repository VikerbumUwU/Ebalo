from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "Ebalo"
    debug: bool = True
    database_url: str = Field(
        default="postgresql+psycopg://user:password@postgres:5432/db",
        alias="DATABASE_URL"
    )
    jwt_key: str = "soros"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()