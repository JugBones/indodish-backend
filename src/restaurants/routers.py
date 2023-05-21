from fastapi import APIRouter, Depends
from src.restaurants import services
from src.restaurants.schemas import CreateRestaurant
from src.dishes.schemas import CreateDish
from src.dishes.dependencies import get_restaurant_id_from_token
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import JWTData

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.post("/register")
async def create_restaurant(
    restaurant_info: CreateRestaurant, jwt_data: JWTData = Depends(parse_jwt_user_data)
):
    return await services.create_restaurant(restaurant_info, jwt_data)


@router.post("/dish")
async def insert_restaurant_dish(
    dish_info: CreateDish, restaurant_id: str = Depends(get_restaurant_id_from_token)
):
    return await services.insert_restaurant_menu(dish_info, restaurant_id)
