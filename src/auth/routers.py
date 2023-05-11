from fastapi import APIRouter, Depends, status, Response, BackgroundTasks
from databases.interfaces import Record
from src.auth import services, utils, jwt
from src.auth.dependencies import (
    valid_user_create,
    valid_refresh_token,
    valid_refresh_token_user,
)
from src.auth.schemas import NewUser, UserLogin, UserResponse, AccessTokenResponse

router = APIRouter(prefix="/auth")


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
async def register_user(
    new_user: NewUser = Depends(valid_user_create),
) -> dict[str, str]:
    user = await services.create_user(new_user)
    return {"email": user["email"]}


@router.post("/tokens", response_model=AccessTokenResponse)
async def authenticate_user(
    user_credential: UserLogin, response: Response
) -> AccessTokenResponse:
    user = await services.authenticate_user(user_credential)
    refresh_token_value = await services.create_refresh_token(user_id=user.id)

    response.set_cookie(**utils.get_refresh_token_settings(refresh_token_value))

    return AccessTokenResponse(
        access_token=jwt.create_access_token(user=user),
        refresh_token=refresh_token_value,
    )


@router.put("/tokens", response_model=AccessTokenResponse)
async def refresh_tokens(
    worker: BackgroundTasks,
    response: Response,
    refresh_token: Record = Depends(valid_refresh_token),
    user: Record = Depends(valid_refresh_token_user),
) -> AccessTokenResponse:
    refresh_token_value = await services.create_refresh_token(user_id=refresh_token.id)

    response.set_cookie(**utils.get_refresh_token_settings(refresh_token_value))

    worker.add_task(services.expire_refresh_token, refresh_token.id)
    return AccessTokenResponse(
        access_token=jwt.create_access_token(user=user),
        refresh_token=refresh_token_value,
    )


@router.delete("tokens")
async def logout_user(
    response: Response, refresh_token: Record = Depends(valid_refresh_token)
) -> None:
    await services.expire_refresh_token(refresh_token.id)

    response.delete_cookie(
        **utils.get_refresh_token_settings(refresh_token.refresh_token), expired=True
    )
