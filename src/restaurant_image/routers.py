from fastapi import APIRouter, File, Depends
from src.auth.schemas import JWTData
from src.auth.jwt import parse_jwt_user_data
from src.restaurant_image import services

router = APIRouter(prefix="/restaurant_image")


@router.post("/")
async def insert_restaurant_image(
    jwt_data: JWTData = Depends(parse_jwt_user_data), image: bytes = File(...)
):
    return await services.insert_image(image)
