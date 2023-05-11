from src import utils
from uuid import uuid4
from datetime import timedelta, datetime
from sqlalchemy import insert, select, update
from databases.interfaces import Record

from src.database import database
from src.auth.config import auth_settings
from src.auth.schemas import NewUser, UserLogin
from src.auth.models import RefreshToken
from src.auth.security import hash_password, check_password
from src.auth.exceptions import InvalidCredentials
from src.users.models import User


async def create_user(new_user: NewUser) -> Record | None:
    insert_query = (
        insert(User)
        .values(
            {
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
                "hashed_password": hash_password(new_user.password),
            }
        )
        .returning(User)
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
    select_query = select(User).where(User.email == email)

    return await database.fetch_one(select_query)


async def get_user_by_id(id: str) -> Record | None:
    select_query = select(User).where(User.id == id)

    return await database.fetch_one(select_query)


async def create_refresh_token(
    *, user_id: str, refresh_token: str | None = None
) -> str:
    if not refresh_token:
        refresh_token = utils.generate_random_alphanumeric(64)

    insert_query = insert(RefreshToken).values(
        {
            "id": uuid4(),
            "refresh_token": refresh_token,
            "expires_at": datetime.utcnow()
            + timedelta(days=auth_settings.REFRESH_TOKEN_EXPIRE_DELTA_DAYS),
            "user_id": user_id,
        }
    )

    await database.execute(insert_query)

    return refresh_token


async def get_refresh_token(refresh_token: str) -> Record | None:
    select_query = select(RefreshToken).where(
        RefreshToken.refresh_token == refresh_token
    )

    return await database.fetch_one(select_query)


async def expire_refresh_token(refresh_token_id: str) -> None:
    update_query = (
        update(RefreshToken)
        .values(
            expires_at=datetime.utcnow()
            - timedelta(days=auth_settings.REFRESH_TOKEN_EXPIRE_DELTA_DAYS)
        )
        .where(RefreshToken.id == refresh_token_id)
    )

    await database.execute(update_query)
