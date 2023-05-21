from pydantic import BaseSettings


class AuthSettings(BaseSettings):
    JWT_ALGORITHM: str

    ACCESS_TOKEN_KEY: str = "access_token"
    ACCESS_TOKEN_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_DELTA_MINUTES: int

    REFRESH_TOKEN_KEY: str = "refresh_token"
    REFRESH_TOKEN_SECRET_KEY: str
    REFRESH_TOKEN_EXPIRE_DELTA_DAYS: int

    SECURE_COOKIES: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


auth_settings = AuthSettings()
