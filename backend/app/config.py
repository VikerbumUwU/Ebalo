from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "Ebalo"
    debug: bool = True
    database_url: str = Field(
        default="postgresql+psycopg://user:password@database:5432/db",
        alias="DATABASE_URL"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()