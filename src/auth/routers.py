from fastapi import APIRouter, Depends, status, Response
from databases.interfaces import Record
from src.auth import services, jwt, config
from src.auth.dependencies import (
    valid_user_create,
    valid_refresh_token,
    valid_refresh_token_user,
)
from src.auth.schemas import (
    NewUser,
    UserLogin,
    UserResponse,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    description="Endpoint for user registration",
)
async def register_user(
    new_user: NewUser = Depends(valid_user_create),
) -> dict[str, str]:
    user = await services.create_user(new_user)
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "restaurant_id": "" if user.restaurant_id is None else user.restaurant_id,
    }


@router.post(
    "/tokens",
    response_model=UserResponse,
    description="Endpoint for sign in",
)
async def authenticate_user(user_credential: UserLogin, response: Response):
    user = await services.authenticate_user(user_credential)
    access_token_value = jwt.create_access_token(user=user)
    refresh_token_value = await services.create_refresh_token(user_id=str(user.id))

    response.set_cookie(
        key="access_token",
        value=access_token_value,
        secure=config.auth_settings.SECURE_COOKIES,
        httponly=True,
        max_age=60 * 5,  # 5 minutes
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token_value,
        secure=config.auth_settings.SECURE_COOKIES,
        httponly=True,
        max_age=60 * 60 * 24 * 7,  # 7 days
    )

    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "restaurant_id": "" if user.restaurant_id is None else str(user.restaurant_id),
    }


@router.put(
    "/tokens",
    response_model=UserResponse,
    description="Endpoint to refresh access tokens",
)
async def refresh_access_token(
    response: Response,
    refresh_token: Record = Depends(valid_refresh_token),
    user: Record = Depends(valid_refresh_token_user),
):
    access_token_value = jwt.create_access_token(user=user)
    response.set_cookie(key="access_token", value=access_token_value, httponly=True)

    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "restaurant_id": "" if user.restaurant_id is None else str(user.restaurant_id),
    }


@router.delete(
    "/tokens",
    description="Endpoint for signing out users, it will expires user's refresh token",
)
async def logout_user(
    response: Response, refresh_token: Record = Depends(valid_refresh_token)
) -> None:
    await services.expire_refresh_token(refresh_token.id)

    response.delete_cookie("access_token", httponly=True)
    response.delete_cookie("refresh_token", httponly=True)
