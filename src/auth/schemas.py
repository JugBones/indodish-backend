from src.schemas import ORJSONModel
from pydantic import EmailStr, root_validator, validator, Field


class NewUser(ORJSONModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    password_confirmation: str

    @validator("password")
    def password_at_least_6_characters(cls, value):
        if len(value) < 6:
            raise ValueError("password must be at least 6 characters")

        return value

    @root_validator()
    def check_password_match(cls, values):
        password, password_confirmation = values.get("password"), values.get(
            "password_confirmation"
        )

        if (
            (password is not None)
            and (password_confirmation is not None)
            and (password != password_confirmation)
        ):
            raise ValueError("passwords do not match")

        return values


class UserLogin(ORJSONModel):
    email: EmailStr
    password: str


class UserResponse(ORJSONModel):
    email: EmailStr


class JWTData(ORJSONModel):
    user_id: str = Field(alias="sub")


class AccessTokenResponse(ORJSONModel):
    access_token: str
    refresh_token: str
