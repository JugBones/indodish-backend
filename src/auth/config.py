from pydantic import BaseSettings


class AuthSettings(BaseSettings):
    ACCESS_TOKEN_SECRET_KEY: str
    REFRESH_TOKEN_SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


auth_settings = AuthSettings()
