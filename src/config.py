from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    SITE_DOMAIN: str
    CORS_HEADERS: list[str]
    CORS_ORIGINS_REGEX: str | None
    CORS_ORIGINS: list[str]
    GEOPY_USER_AGENT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
