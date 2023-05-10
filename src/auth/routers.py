from fastapi import APIRouter, Depends, status
from src.auth.schemas import NewUser, UserResponse
from src.auth import services
from src.auth.dependencies import valid_user_create

router = APIRouter(prefix="/auth")


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
async def register_user(
    new_user: NewUser = Depends(valid_user_create),
) -> dict[str, str]:
    user = await services.create_user(new_user)
    return {"email": user["email"]}
