from src import utils
from datetime import timedelta, datetime
from sqlalchemy import insert
from databases.interfaces import Record

from jose import jwt
from src.database import database
from src.auth.config import auth_settings
from src.auth.schemas import NewUser, UserLogin
from src.auth.models import refresh_token
from src.auth.security import hash_password, check_password
from src.auth.exceptions import InvalidCredentials
from src.users.models import user


async def create_user(new_user: NewUser) -> Record | None:
    insert_query = (
        insert(user)
        .values(
            {
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
                "hashed_password": hash_password(new_user.password),
            }
        )
        .returning(user)
    )

    return await database.fetch_one(insert_query)


async def authenticate_user(user_credential: UserLogin) -> Record:
    user = await get_user_by_email(user_credential.email)
    if not user:
        raise InvalidCredentials()

    if not check_password(user_credential.password, user.hashed_password):
        raise InvalidCredentials()

    return user


async def get_user_by_email(email: str) -> Record | None:
    select_query = user.select().where(user.c.email == email)

    return await database.fetch_one(select_query)


async def get_user_by_id(id: str) -> Record | None:
    select_query = user.select().where(user.c.id == id)

    return await database.fetch_one(select_query)


async def create_refresh_token(
    *,
    user_id: str,
    refresh_token_value: str | None = None,
    expires_delta: timedelta = timedelta(
        days=auth_settings.REFRESH_TOKEN_EXPIRE_DELTA_DAYS
    ),
):
    jwt_data = {
        "sub": utils.generate_random_alphanumeric(64),
        "user_id": user_id,
        "exp": datetime.utcnow() + expires_delta,
    }

    insert_query = insert(refresh_token).values(
        {
            "user_id": jwt_data["user_id"],
            "refresh_token": jwt_data["sub"],
            "expired_at": jwt_data["exp"],
        }
    )

    await database.execute(insert_query)

    return jwt.encode(
        claims=jwt_data,
        key=auth_settings.REFRESH_TOKEN_SECRET_KEY,
        algorithm=auth_settings.JWT_ALGORITHM,
    )


async def get_refresh_token(refresh_token_value: str) -> Record | None:
    if refresh_token_value is None:
        return None

    jwt_data = jwt.decode(refresh_token_value, auth_settings.REFRESH_TOKEN_SECRET_KEY)

    select_query = refresh_token.select().where(
        refresh_token.c.refresh_token == jwt_data["sub"]
    )

    return await database.fetch_one(select_query)


async def expire_refresh_token(refresh_token_id: str) -> None:
    delete_query = refresh_token.delete().where(refresh_token.c.id == refresh_token_id)

    await database.execute(delete_query)
