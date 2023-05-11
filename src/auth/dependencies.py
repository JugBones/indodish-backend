from typing import Annotated
from fastapi import Cookie, Depends

from datetime import datetime
from databases.interfaces import Record

from src.auth import services
from src.auth.schemas import NewUser
from src.auth.exceptions import EmailTaken, RefreshTokenNotValid


async def valid_user_create(new_user: NewUser):
    if await services.get_user_by_email(new_user.email):
        raise EmailTaken()

    return new_user


async def valid_refresh_token(refresh_token: Annotated[str, Cookie()]) -> Record:
    db_refresh_token = await services.get_refresh_token(refresh_token)
    if not db_refresh_token:
        raise RefreshTokenNotValid()

    if not _is_valid_refresh_token(refresh_token):
        raise RefreshTokenNotValid()

    return db_refresh_token


async def valid_refresh_token_user(
    refresh_token: Record = Depends(valid_refresh_token),
) -> Record:
    user = await services.get_user_by_id(refresh_token.user_id)
    if not user:
        raise RefreshTokenNotValid()

    return user


def _is_valid_refresh_token(db_refresh_token: Record) -> bool:
    return datetime.utcnow() <= db_refresh_token.expires_at
