from fastapi import APIRouter, Depends
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import JWTData
from src.cart import services
from src.cart.schemas import InsertDishToCart, UpdateCartItem, RemoveDishFromCart

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/")
async def get_user_cart(jwt_data: JWTData = Depends(parse_jwt_user_data)):
    return await services.get_from_cart(jwt_data)


@router.post("/")
async def insert_dish_to_cart(
    dish_info: InsertDishToCart, jwt_data: JWTData = Depends(parse_jwt_user_data)
):
    return await services.upsert_to_cart(jwt_data, dish_info)


@router.post("/")
async def update_dish_from_cart(
    dish_info: UpdateCartItem, jwt_data: JWTData = Depends(parse_jwt_user_data)
):
    return await services.update_to_cart(jwt_data, dish_info)


@router.delete("/")
async def remove_dish_from_cart(
    dish_info: RemoveDishFromCart, jwt_data: JWTData = Depends(parse_jwt_user_data)
):
    return await services.remove_from_cart(jwt_data, dish_info)
