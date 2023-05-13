from fastapi import APIRouter, Depends

from src.auth.schemas import JWTData
from src.auth.jwt import parse_jwt_user_data

from src.users import services
from src.users.schemas import UserProfileUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.put("/profile")
async def edit_profile(
    user_profile: UserProfileUpdate, jwt_data: JWTData = Depends(parse_jwt_user_data)
):
    return await services.update_user_profile(jwt_data.user_id, user_profile)
