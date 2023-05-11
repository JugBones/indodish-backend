from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from databases.interfaces import Record

from src.auth.schemas import JWTData
from src.auth.config import auth_settings
from src.auth.exceptions import InvalidToken, AuthRequired

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/tokens", auto_error=False)


def create_access_token(
    user: Record,
    expires_delta: timedelta = timedelta(
        minutes=auth_settings.ACCESS_TOKEN_EXPIRE_DELTA_MINUTES
    ),
) -> str:
    jwt_data = {"sub": str(user.id), "exp": datetime.utcnow() + expires_delta}

    return jwt.encode(
        claims=jwt_data,
        key=auth_settings.ACCESS_TOKEN_SECRET_KEY,
        algorithm=auth_settings.JWT_ALGORITHM,
    )


async def parse_jwt_user_data_optional(
    token: str = Depends(oauth2_scheme),
) -> JWTData | None:
    if not token:
        return None

    try:
        payload = jwt.decode(
            token,
            auth_settings.ACCESS_TOKEN_SECRET_KEY,
            algorithms=[auth_settings.JWT_ALGORITHM],
        )

    except JWTError:
        raise InvalidToken()

    return JWTData(**payload)


async def parse_jwt_user_data(
    token: JWTData | None = Depends(parse_jwt_user_data_optional),
) -> JWTData:
    if not token:
        raise AuthRequired()

    return token
