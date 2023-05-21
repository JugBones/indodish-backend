from typing import Annotated
from fastapi import Depends
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import JWTData


async def get_restaurant_id_from_token(
    jwt_data: Annotated[JWTData, Depends(parse_jwt_user_data)] = None
):
    if jwt_data is None:
        return None
    print(jwt_data.restaurant_id)
    return jwt_data.restaurant_id
